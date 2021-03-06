#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

import logging
import os
import sys
import threading
import time

import PySide.QtCore    as QtCore
import PySide.QtGui     as QtGui
from   PySide           import QtSvg, QtXml

import configuration    as config
from   pydash_gui       import Ui_pydash
import twitch

scopes = sorted([u"user_read", u"channel_editor", u"channel_commercial", u"chat_login"])

logging.getLogger("requests").setLevel(logging.WARNING)

image_folder = "images"
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

class SignalCollection(QtCore.QObject):

    auth_set       = QtCore.Signal(str)
    nick_set       = QtCore.Signal(str)
    title_set      = QtCore.Signal(str)
    game_set       = QtCore.Signal(str)
    status_set     = QtCore.Signal(str)
    update_status  = QtCore.Signal()
    update_hosts   = QtCore.Signal(str)

    show_new_message = QtCore.Signal(str)
    update_msg_time  = QtCore.Signal(str)

class Dashboard(QtGui.QMainWindow, Ui_pydash):

    def __init__(self, parent = None):
        super(Dashboard, self).__init__(parent)
        self.setupUi(self)

        self.authorized = False
        self.chat_connected = False
        self.partner = False
        self.live = False
        self.peak_viewer = 0
        self.last_message = int(time.time())

        self.configure = config.Configurer()
        self.signals = SignalCollection()

        #set up labels for status bar
        self.status_hosts = QtGui.QLabel(self.centralwidget)
        self.status_hosts.setObjectName("status_host_text")
        self.statusBar.addPermanentWidget(self.status_hosts)
        self.status_bools = QtGui.QLabel(self.centralwidget)
        self.status_bools.setObjectName("status_bool_text")
        self.statusBar.addPermanentWidget(self.status_bools)

        self.authorize_button.clicked.connect(self.configure.get_auth_code)
        self.auth_input.returnPressed.connect(self.check_code)
        self.oauth_get.clicked.connect(self.check_code)
        self.chat_connect.clicked.connect(self.connect_to_chat)

        self.ad_30.clicked.connect(self.ad_click)
        self.ad_60.clicked.connect(self.ad_click)
        self.ad_90.clicked.connect(self.ad_click)
        self.ad_120.clicked.connect(self.ad_click)
        self.ad_150.clicked.connect(self.ad_click)
        self.ad_180.clicked.connect(self.ad_click)

        self.refresh.clicked.connect(self.refresh_gt)
        self.update_game_title.clicked.connect(self.set_game_title)

        self.chat_send.returnPressed.connect(self.message_send)
        self.send_message.clicked.connect(self.message_send)

        self.signals.auth_set.connect(self.set_auth_text)
        self.signals.nick_set.connect(self.set_nick_text)
        self.signals.title_set.connect(self.set_title_text)
        self.signals.game_set.connect(self.set_game_text)
        self.signals.status_set.connect(self.status_temp_text)
        self.signals.update_status.connect(self.set_status_bools)
        self.signals.update_hosts.connect(self.set_status_hosts)
        self.signals.show_new_message.connect(self.set_new_message)
        self.signals.update_msg_time.connect(self.update_last_message)

        self.user_config = self.configure.load_file()
        if self.user_config["debug"]:
            logging.basicConfig(filename='debug.log', filemode='w', level=logging.INFO)

        self.setGeometry(self.user_config["position"][0], self.user_config["position"][1], self.user_config["size"][0], self.user_config["size"][1])
        self.signals.update_status.emit()
        self.signals.update_hosts.emit("None")

        if self.user_config["oauth"] != "":
            self.signals.auth_set.emit(self.user_config["oauth"])
            checker = threading.Thread(target=self.check_code)
            checker.daemon = True
            checker.start()

        auto_minute = threading.Thread(target=self.minute_loop)
        auto_minute.daemon = True
        auto_minute.start()

    def check_code(self):
        if not self.authorized:
            oauth = self.auth_input.text()
            if oauth == "":
                self.signals.status_set.emit("Please actually enter and oauth token.")
                return
            self.api_worker = twitch.API(oauth)
            self.api_worker.set_oauth_header(oauth)
            try:
                info = self.api_worker.check_auth_status()
            except Exception, e:
                logging.exception(e)
                self.check_code()
            if info:
                if info["token"]["valid"] and sorted(info["token"]["authorization"]["scopes"]) == scopes:
                    self.authorized = True
                    self.user_config = self.configure.set_param("channel", info["token"]["user_name"])
                    self.user_config = self.configure.set_param("oauth", oauth)
                    if not self.user_config["twitch_id"]:
                        twitch_id = self.api_worker.get_twitch_id(info["token"]["user_name"])["_id"]
                        if twitch_id:
                            self.configure.set_param("twitch_id", twitch_id)
                    self.signals.nick_set.emit(info["token"]["user_name"])
                    self.api_worker.channel = self.user_config["channel"]
                    self.auth_input.setReadOnly(True)
                    self.refresh_gt()
                    self.partner = self.api_worker.check_partner_status()
                    if self.partner:
                        logging.info("User is partner, enabling ad buttons.")
                        self.signals.status_set.emit("Authenticated | Partner: Commercial Buttons Enabled")
                        self.ad_30.setEnabled(True)
                        self.ad_60.setEnabled(True)
                        self.ad_90.setEnabled(True)
                        self.ad_120.setEnabled(True)
                        self.ad_150.setEnabled(True)
                        self.ad_180.setEnabled(True)
                    else:
                        self.signals.status_set.emit("Authenticated")
                else:
                    self.signals.status_set.emit("Bad OAuth, Please Retrieve Another")
                    self.auth_input.setText("")
            else:
                self.signals.status_set.emit("There was an error connecting to Twitch API, please try again.")
        self.signals.update_status.emit()
        return

    def set_completer(self):
        #set up auto-complete for game if it is present
        self.games_list = self.configure.get_completer_list()
        if self.games_list:
            self.game_completer = QtGui.QCompleter(self.games_list, self.game)
            self.game_completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
            self.game_completer.setModelSorting(QtGui.QCompleter.CaseSensitivelySortedModel)
            self.game.setCompleter(self.game_completer)

    def connect_to_chat(self):
        if self.authorized:
            if self.chat_connected:
                self.chat_connected = False
                self.chat_worker.running = False
                self.chat_worker.irc_disconnect()
                del self.chat_worker
                self.chat_connect.setText("Connect to Chat")
                self.send_message.setEnabled(False)
                self.signals.show_new_message.emit('<div style="margin-top: 2px; margin-bottom: 2px; color: #858585;">Disconnected from chat.</div>')
                self.signals.update_status.emit()
            else:
                nick = self.nick.text()
                oauth = self.api_worker.oauth_token
                self.chat_worker = twitch.Chat(nick, oauth, self.signals)
                logging.info("Starting chatter thread")
                self.chatter = threading.Thread(target=self.chat_worker.init_icons, args=(self.partner, self.chat_worker.main_loop))
                self.chatter.daemon = True
                self.chatter.start()
                self.chat_connected = True
                self.chat_connect.setText("Disconnect")
                self.signals.update_status.emit()
                self.send_message.setEnabled(True)

    @QtCore.Slot(str)
    def set_auth_text(self, text):
        self.auth_input.setText(text)

    @QtCore.Slot(str)
    def set_nick_text(self, text):
        self.nick.setText(text)

    @QtCore.Slot(str)
    def set_title_text(self, text):
        self.title.setPlainText(text)

    @QtCore.Slot(str)
    def set_game_text(self, text):
        self.game.setText(text)

    @QtCore.Slot(str)
    def status_temp_text(self, text):
        self.statusBar.showMessage(text)

    @QtCore.Slot()
    def set_status_bools(self):
        self.status_bools.setText("Live: " + str(self.live))

    @QtCore.Slot(str)
    def set_status_hosts(self, hosters):
        self.status_hosts.setText("Hosters: " + hosters)

    @QtCore.Slot(str)
    def set_new_message(self, msg):
        self.chat_box.append(msg)

    @QtCore.Slot(str)
    def update_last_message(self, time_sent):
        self.last_message = time_sent

    def ad_click(self):
        if self.authorized and self.partner:
            length = int(self.sender().text())
            success = self.api_worker.run_commercial(length)
            if success:
                ad_thread = threading.Thread(self.ad_cooldown, args=length)
                ad_thread.daemon = True
                ad_thread.start()
            else:
                self.signals.status_set.emit("Commercial Failed to Run")

    def set_game_title(self):
        if self.authorized:
            self.signals.status_set.emit("Updating Game and Title...")
            title = self.title.toPlainText().strip()
            game = self.game.text().strip()
            success = self.api_worker.set_gt(title, game)
            if success["game"] == game and success["status"] == title:
                self.signals.status_set.emit("Updated Game and Title")
            else:
                self.signals.status_set.emit("Failed to Updated Game and Title")

    def refresh_gt(self):
        if self.authorized:
            self.signals.status_set.emit("Refreshing Game and Title...")
            title, game = self.api_worker.get_gt()
            if title and game:
                self.signals.title_set.emit(title)
                self.signals.game_set.emit(game)
                self.signals.status_set.emit("Game and Title Refreshed")
            else:
                self.signals.status_set.emit("Failed to Refresh")

    def message_send(self):
        if self.chat_connected:
            msg = self.chat_send.text().encode("utf-8")
            self.chat_send.setText("")
            if msg:
                self.chat_worker.send_msg(msg)
        else:
            self.chat_send.setText("")

    def ad_cooldown(self, length):
        current_status = self.statusBar.currentMessage()
        while length > 0:
            if current_status:
                current_status = current_status.split(" | ")[0]
                self.signals.status_set.emit(current_status + " | Last Ad: " + str(length))
            else:
                self.signals.status_set.emit("Last Ad: " + length)
            length -= length
            time.sleep(1)
        return

    def minute_loop(self):
        time.sleep(5)
        while True:
            if self.authorized:
                info = self.api_worker.get_stream_object()
                if info:
                    if info["stream"] != None:
                        self.live = True
                        viewers = info["stream"]["viewers"]
                        self.viewer_number.setText(str(viewers))
                        if viewers > self.peak_viewer:
                            self.peak_viewer_number.setText(str(viewers))
                            self.peak_viewer = viewers
                        if viewers > self.user_config["max_viewers"]:
                            self.user_config = self.configure.set_param("max_viewers", viewers)
                    else:
                        self.live = False
                        self.viewer_number.setText('0')
                if self.user_config["twitch_id"]:
                    hosters_obj = self.api_worker.get_hosting_object(self.user_config["twitch_id"])
                    if hosters_obj and hosters_obj["hosts"]:
                        hosters = [i["host_login"] for i in hosters_obj["hosts"]]
                        if hosters:
                            hosters_string = ", ".join(hosters)
                            self.set_status_hosts(hosters_string)
                        else:
                            self.set_status_hosts("None")

                current_time = int(time.time())
                if self.chat_connected and self.last_message < (current_time + 60):
                    try:
                        self.chat_worker.send_ping()
                        self.last_message = current_time
                    except Exception:
                        pass

            self.signals.update_status.emit()
            time.sleep(60)

    def closeEvent(self, event):
        for files in os.listdir(image_folder):
            file_path = os.path.join(image_folder, files)
            try:
                os.unlink(file_path)
            except Exception, e:
                logging.exception(e)

        if self.chat_connected:
            try:
                self.chat_worker.irc_disconnect()
            except Exception, e:
                pass

        position = [self.pos().x(), self.pos().y()]
        size = [self.size().width(), self.size().height()]
        self.user_config = self.configure.set_param("position", (position))
        self.user_config = self.configure.set_param("size", (size))
        QtGui.QMainWindow.closeEvent(self, event)


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    window = Dashboard()
    window.show()
    window.set_completer()
    sys.exit(app.exec_())
