#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

import logging
import json
import os
import Queue
import re
import shutil
import socket
import time

import requests

os.environ['REQUESTS_CA_BUNDLE'] = 'cacert.pem'

class API:

    def __init__(self, token, channel = ""):
        self.oauth_token = token
        self.channel = channel
        self.base_url = "https://api.twitch.tv/kraken"
        self.last_commercial = 0
        self.headers = {}

    def set_headers(self, oauth):
        self.headers = {"Accept" : "application/vnd.twitchtv.v3+json", "Authorization" : "OAuth " + oauth}

    def check_auth_status(self):
        endpoint = '/'
        info = self.api_call("get", endpoint = endpoint)
        if info:
            return info
        else:
            return False

    def check_partner_status(self):
        endpoint = "/user"
        info = self.api_call("get", endpoint = endpoint)
        if info:
            return info["partnered"]
        else:
            return False

    def json_decode(self, json_object):
        if json_object.status_code == 200:
            json_decode = json_object.json()
            return json_decode
        else:
            return False

    def api_call(self, method, endpoint, data = None):
        url = self.base_url + endpoint

        try:
            if method == "get":
                info = requests.get(url, headers = self.headers)
            elif method == "post":
                info = requests.post(url ,headers = self.headers, data = data)
            elif method == "put":
                info = requests.put(url, headers = self.headers, data = data)
            else:
                raise Exception
            info.raise_for_status()
            info_decode = self.json_decode(info)
            return info_decode
        except Exception, e:
            logging.exception("API class api_call method")
            return False

    def get_gt(self):
        endpoint = "/channels/" + self.channel
        info = self.api_call("get", endpoint = endpoint)
        if info:
            return info["status"], info["game"]
        else:
            return False, False

    def set_gt(self, title, game):
        endpoint = "/channels/" + self.channel
        params = {u"channel[status]" : title, u"channel[game]" : game}
        return_info = self.api_call("put", endpoint, params)
        return return_info

    def get_stream_object(self):
        endpoint = "/streams/" + self.channel
        info = self.api_call("get", endpoint = endpoint)
        if info:
            return info
        else:
            return False

    def get_hosting_object(self):
        hosters = requests.get("https://chatdepot.twitch.tv/rooms/{}/hosts".format(self.channel))
        return self.json_decode(hosters)

    def run_commercial(self, length):
        if time.time() - self.last_commercial > 480:
            new_info = {"length" : length}
            endpoint = "/channels/{}/commercial".format(self.channel)
            success = self.api_call("post", endpoint, new_info)
            if success:
                self.last_commercial = int(time.time())
            return success

class Chat:

    def __init__(self, name, oauth, q):
        self.channel = name
        self.oauth = "oauth:" + oauth
        self.q = q
        self.running = False
        self.badges = {}
        self.emotes_dict = {}
        self.ffz_url = "http://cdn.frankerfacez.com/channel"
        self.ffz_emotes = []
        self.ffz_g_emotes = ["BeanieHipster", "LilZ", "ManChicken", "YellowFever", "YooHoo", "ZreknarF"]
        self.ffz_dict = {}
        self.custom_mod = False
        logging.info("Chat object initialized")

    def init_icons(self, partner, start_loop_func):
        logging.info("Init icons started")
        self.ffz_check()
        self.get_chat_badges()
        if partner and not os.path.exists("images/sub_icon.png"):
            self.get_sub_badge()
            logging.info("Sub badge loaded")
        logging.info("Launching main loop from init_icons")
        start_loop_func()

    def ffz_check(self):
        url = "{}/{}.css".format(self.ffz_url, self.channel)
        data = requests.get(url)
        if data.status_code == 200:
            if data.text.endswith("!important"):
                self.custom_mod = True

            emotes = re.findall('{content:"(.+?)";', data.text)
            for i in emotes:
                self.ffz_emotes.append(i)
        else:
            logging.info("FFZ did not return a 200.")

    def save_chat_badges(self, url, key, f_name):
        image = requests.get(url, stream = True)
        with open(f_name, "wb") as i_file:
            shutil.copyfileobj(image.raw, i_file)
        self.badges[key] = f_name

    def get_chat_badges(self):
        logging.info("Retrieving Chat Badges")
        if not os.path.exists("images/broadcaster_icon.png"):
            bc_url = "http://chat-badges.s3.amazonaws.com/broadcaster.png"
            self.save_chat_badges(bc_url, "broadcaster", "images/broadcaster_icon.png")

        if not os.path.exists("/images/mod_icon.png"):
            if self.custom_mod:
                mod_url = self.ffz_url + "/" + self.channel + "/mod_icon.png"
            else:
                mod_url = "http://chat-badges.s3.amazonaws.com/mod.png"
            self.save_chat_badges(mod_url, "mod", "images/mod_icon.png")

        if not os.path.exists("images/broadcaster_icon.png"):
            staff_url = "http://chat-badges.s3.amazonaws.com/staff.png"
            self.save_chat_badges(staff_url, "staff", "images/staff_icon.png")

        if not os.path.exists("images/global_mod.png"):
            global_url = "http://chat-badges.s3.amazonaws.com/globalmod.png"
            self.save_chat_badges(global_url, "global_mod", "images/global_mod.png")

        if not os.path.exists("images/turbo_icon.png"):
            turbo_url = "http://chat-badges.s3.amazonaws.com/turbo.png"
            self.save_chat_badges(turbo_url, "turbo", "images/turbo_icon.png")
        logging.info("Chat Badges Downloaded")

    def get_sub_badge(self):
        logging.info("Retrieving Sub Badge")
        url = "https://api.twitch.tv/kraken/chat/{}/badges".format(self.channel)
        badge_links = requests.get(url)
        self.save_chat_badges(badge_links["subscriber"]["image"], "subscriber", "images/sub_icon.png")
        logging.info("Sub Badge Downloaded")

    def connect(self):
        logging.info("Connecting to Twitch")
        twitch_host = "irc.twitch.tv"
        twitch_port = 6667
        self.irc = socket.socket()
        self.irc.settimeout(600)
        self.irc.connect((twitch_host, twitch_port))
        logging.info("Connection Complete")

    def irc_disconnect(self):
        try:
            self.irc.sendall("QUIT\r\n")
        except Exception:
            pass
        self.irc.close()

    def send_irc_auth(self):
        logging.info("Sending Authentication")
        self.irc.sendall("PASS {}\r\n".format(self.oauth))
        self.irc.sendall("NICK {}\r\n".format(self.channel))
        logging.info("Authentication Sent")

    def join_channel(self):
        logging.info("Joining Channel and Getting Tags")
        self.irc.sendall("JOIN #{}\r\n".format(self.channel))
        self.irc.sendall('CAP REQ :twitch.tv/tags\r\n')
        logging.info("Joined Channel and Requested Tags")

    def establish_connection(self):
        self.connect()
        self.send_irc_auth()
        success = self.irc.recv(4096)
        logging.info("Retrieving Initial Messages")
        logging.debug(success)
        if success == ":tmi.twitch.tv NOTICE * :Login unsuccessful\r\n":
            raise Exception
        time.sleep(1)
        self.join_channel()

    def send_msg(self, txt):
        self.irc.sendall("PRIVMSG #{} :{}\r\n".format(self.channel, txt))
        return True

    def get_emote_key(self, key, e_dict, url):
        try:
            image_file = e_dict[key]
        except KeyError:
            print url
            try:
                image = requests.get(url, stream = True)
                image.raise_for_status()
                with open("images/" + key + ".png", 'wb') as i_file:
                    image.raw.decode_content = True
                    shutil.copyfileobj(image.raw, i_file)
                image_file = e_dict[key] = "images/" + key + ".png"
            except Exception:
                logging.exception("Error getting emote image from cdn")
                image_file = key
        return image_file

    def badge_html(self, badge_file):
        return '<img src="{}" height="18" width="18" /> '.format(badge_file)

    def twitch_badges(self, msg_dict):
        badges = ''
        m_tags = msg_dict["tags"]

        if msg_dict["sender"] == self.channel:
            badges += self.badge_html(self.badges["broadcaster"])
        elif m_tags["user_type"]:
            if m_tags["user_type"] == "staff":
                badges += self.badge_html(self.badges["staff"])
            elif m_tags["user_type"] == "admin":
                badges += self.badge_html(self.badges["admin"])
            elif m_tags["user_type"] == "global_mod":
                badges += self.badge_html(self.badges["global_mod"])
            elif m_tags["user_type"] == "mod":
                badges += self.badge_html(self.badges["mod"])

        if m_tags["turbo"] == '1':
            badges += self.badge_html(self.badges["turbo"])
        if m_tags["subscriber"] == '1':
            badges += self.badge_html(self.badges["subscriber"])

        return badges

    def twitch_emote_parse(self, msg, e_tags):
        if not e_tags["emotes"]:
            return msg

        emotes = []
        e_array = e_tags["emotes"].split('/')

        for i in e_array:
            tmp = i.split(':')
            emotes.append({tmp[0] : tmp[1]})

        emotes_long = []
        for i in emotes:
            for k, v in i.iteritems():
                tmp = v.split(',')
                for i in tmp:
                    emotes_long.append({k : i})

        emotes_sorted = sorted(emotes_long, key=lambda k: int(k.values()[0].split('-')[0]), reverse=True) 
        for i in emotes_sorted:
            for k, v in i.iteritems():
                emote_url = "http://static-cdn.jtvnw.net/emoticons/v1/{}/1.0".format(k)
                image_file = self.get_emote_key(k, self.emotes_dict, emote_url)
                emote_replace = '<img src="{}" />'.format(image_file)
                e_range = v.split('-')
                msg = msg[0:int(e_range[0])] + emote_replace + msg[(int(e_range[1]) + 1):]

        return msg

    def ffz_parse(self, msg):
        for i in self.ffz_emotes:
            if i in msg:
                emote_url = self.ffz_url + '/' + self.channel + '/' + i + ".png"
                image_file = self.get_emote_key(i, self.ffz_dict, emote_url)
                emote_replace = '<img src="{}" />'.format(image_file)
                msg = msg.replace(i, emote_replace)

        for i in self.ffz_g_emotes:
            if i in msg:
                emote_url = "{}/global/{}.png".format(self.ffz_url, i)
                image_file = self.get_emote_key(i, self.ffz_dict, emote_url)
                emote_replace = '<img src="{}" />'.format(image_file)
                msg = msg.replace(i, emote_replace)
        return msg

    def parse_msg(self, msg_dict):
        badges = self.twitch_badges(msg_dict)
        twitch_e_msg = self.twitch_emote_parse(msg_dict["message"], msg_dict["tags"])
        twitch_ffz_msg = self.ffz_parse(twitch_e_msg)
        msg_time = self.get_timestamp()
        final_msg = '<div style="margin-top: 2px; margin-bottom: 2px;"><span style="font-size: 6pt;">{}</span> {}<span style="color: {};">{}</span>: {}</div>'\
                    .format(msg_time, badges, msg_dict["tags"]["color"], msg_dict["sender"], twitch_ffz_msg)
        return final_msg

    def get_timestamp(self):
        msg_time = time.strftime("%I:%M")
        if msg_time.startswith('0'):
            msg_time = msg_time[1:]
        return msg_time

    def main_loop(self):
        logging.info("Main Loop Started")
        self.establish_connection()
        self.running = True
        self.q.put('<div style="margin-top: 2px; margin-bottom: 2px; color: #858585;">Connected to chat!</div>')
        logging.info("Entering main_loop while loop")
        while self.running:
            try:
                message = self.irc.recv(4096)
            except socket.timeout:
                self.establish_connection()

            if message:
                if message.startswith("PING"):
                    self.irc.sendall("PONG tmi.twitch.tv\r\n")
                    continue

                if message == "":
                    self.irc_disconnect()
                    self.establish_connection()
                    continue
                elif message.startswith(":jtv!"):
                    message = message.strip()
                    msg_type = message.split(' ')
                    print msg_type
                    if msg_type[1] == "PRIVMSG" and msg_type[2] == self.channel:
                        send_msg = ' '.join(msg_type[3:])[1:]
                        self.q.put('<div style="margin-top: 2px; margin-bottom: 2px;"><span style="font-size: 6pt;">{}</span> <span style="color: #858585;">{}</span></div>'\
                                   .format(self.get_timestamp(), send_msg))
                        continue

                try:
                    action = message.split(' ')[2]
                except:
                    print message
                    continue
                if action == "PRIVMSG":
                    msg_parts = message.split(' ')
                    c_msg = {}
                    c_msg["tags"] = dict(item.split('=') for item in msg_parts[0][1:].split(';'))
                    c_msg["sender"] = msg_parts[1][1:].split('!')[0]
                    c_msg["action"] = msg_parts[2]
                    c_msg["channel"] = msg_parts[3]
                    c_msg["message"] = ' '.join(msg_parts[4:])[1:].strip()
                    print c_msg
                    self.q.put(self.parse_msg(c_msg))
