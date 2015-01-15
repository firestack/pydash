# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pdashboard_gui.ui'
#
# Created: Thu Jan 15 10:11:36 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_pdt(object):
    def setupUi(self, pdt):
        pdt.setObjectName("pdt")
        pdt.resize(850, 385)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pdt.sizePolicy().hasHeightForWidth())
        pdt.setSizePolicy(sizePolicy)
        pdt.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        pdt.setFont(font)
        pdt.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        pdt.setDocumentMode(False)
        pdt.setTabShape(QtGui.QTabWidget.Rounded)
        pdt.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(pdt)
        self.centralwidget.setObjectName("centralwidget")
        self.update_game_title = QtGui.QPushButton(self.centralwidget)
        self.update_game_title.setGeometry(QtCore.QRect(330, 140, 111, 141))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_game_title.sizePolicy().hasHeightForWidth())
        self.update_game_title.setSizePolicy(sizePolicy)
        self.update_game_title.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.update_game_title.setFont(font)
        self.update_game_title.setObjectName("update_game_title")
        self.oauth_get = QtGui.QPushButton(self.centralwidget)
        self.oauth_get.setGeometry(QtCore.QRect(330, 50, 111, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oauth_get.sizePolicy().hasHeightForWidth())
        self.oauth_get.setSizePolicy(sizePolicy)
        self.oauth_get.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.oauth_get.setFont(font)
        self.oauth_get.setObjectName("oauth_get")
        self.title_label = QtGui.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(10, 180, 46, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setScaledContents(True)
        self.title_label.setObjectName("title_label")
        self.nick_label = QtGui.QLabel(self.centralwidget)
        self.nick_label.setGeometry(QtCore.QRect(10, 50, 46, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nick_label.sizePolicy().hasHeightForWidth())
        self.nick_label.setSizePolicy(sizePolicy)
        self.nick_label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.nick_label.setFont(font)
        self.nick_label.setFrameShadow(QtGui.QFrame.Plain)
        self.nick_label.setScaledContents(True)
        self.nick_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nick_label.setObjectName("nick_label")
        self.viewer_text = QtGui.QLabel(self.centralwidget)
        self.viewer_text.setEnabled(True)
        self.viewer_text.setGeometry(QtCore.QRect(70, 290, 211, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewer_text.sizePolicy().hasHeightForWidth())
        self.viewer_text.setSizePolicy(sizePolicy)
        self.viewer_text.setSizeIncrement(QtCore.QSize(0, 0))
        self.viewer_text.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setWeight(75)
        font.setBold(True)
        self.viewer_text.setFont(font)
        self.viewer_text.setFrameShadow(QtGui.QFrame.Plain)
        self.viewer_text.setScaledContents(True)
        self.viewer_text.setAlignment(QtCore.Qt.AlignCenter)
        self.viewer_text.setMargin(0)
        self.viewer_text.setIndent(-1)
        self.viewer_text.setObjectName("viewer_text")
        self.chat_container = QtGui.QGroupBox(self.centralwidget)
        self.chat_container.setGeometry(QtCore.QRect(450, 0, 391, 361))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat_container.sizePolicy().hasHeightForWidth())
        self.chat_container.setSizePolicy(sizePolicy)
        self.chat_container.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.chat_container.setFont(font)
        self.chat_container.setAcceptDrops(True)
        self.chat_container.setFlat(False)
        self.chat_container.setObjectName("chat_container")
        self.send_message = QtGui.QPushButton(self.chat_container)
        self.send_message.setEnabled(False)
        self.send_message.setGeometry(QtCore.QRect(340, 320, 41, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_message.sizePolicy().hasHeightForWidth())
        self.send_message.setSizePolicy(sizePolicy)
        self.send_message.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.send_message.setFont(font)
        self.send_message.setObjectName("send_message")
        self.chat_send = QtGui.QLineEdit(self.chat_container)
        self.chat_send.setGeometry(QtCore.QRect(10, 320, 321, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat_send.sizePolicy().hasHeightForWidth())
        self.chat_send.setSizePolicy(sizePolicy)
        self.chat_send.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chat_send.setFont(font)
        self.chat_send.setDragEnabled(True)
        self.chat_send.setObjectName("chat_send")
        self.chat_box = QtGui.QTextEdit(self.chat_container)
        self.chat_box.setGeometry(QtCore.QRect(10, 20, 371, 291))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat_box.sizePolicy().hasHeightForWidth())
        self.chat_box.setSizePolicy(sizePolicy)
        self.chat_box.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.chat_box.setFont(font)
        self.chat_box.setAcceptDrops(False)
        self.chat_box.setFrameShape(QtGui.QFrame.StyledPanel)
        self.chat_box.setFrameShadow(QtGui.QFrame.Sunken)
        self.chat_box.setLineWidth(1)
        self.chat_box.setMidLineWidth(0)
        self.chat_box.setReadOnly(True)
        self.chat_box.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.chat_box.setObjectName("chat_box")
        self.game_label = QtGui.QLabel(self.centralwidget)
        self.game_label.setGeometry(QtCore.QRect(10, 140, 46, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_label.sizePolicy().hasHeightForWidth())
        self.game_label.setSizePolicy(sizePolicy)
        self.game_label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.game_label.setFont(font)
        self.game_label.setScaledContents(True)
        self.game_label.setObjectName("game_label")
        self.refresh = QtGui.QToolButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(10, 220, 51, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh.sizePolicy().hasHeightForWidth())
        self.refresh.setSizePolicy(sizePolicy)
        self.refresh.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.refresh.setFont(font)
        self.refresh.setObjectName("refresh")
        self.nick = QtGui.QLineEdit(self.centralwidget)
        self.nick.setGeometry(QtCore.QRect(70, 50, 251, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nick.sizePolicy().hasHeightForWidth())
        self.nick.setSizePolicy(sizePolicy)
        self.nick.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nick.setFont(font)
        self.nick.setMouseTracking(False)
        self.nick.setAcceptDrops(False)
        self.nick.setReadOnly(True)
        self.nick.setObjectName("nick")
        self.game = QtGui.QLineEdit(self.centralwidget)
        self.game.setGeometry(QtCore.QRect(70, 140, 251, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game.sizePolicy().hasHeightForWidth())
        self.game.setSizePolicy(sizePolicy)
        self.game.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.game.setFont(font)
        self.game.setObjectName("game")
        self.auth_code = QtGui.QLabel(self.centralwidget)
        self.auth_code.setGeometry(QtCore.QRect(10, 10, 51, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auth_code.sizePolicy().hasHeightForWidth())
        self.auth_code.setSizePolicy(sizePolicy)
        self.auth_code.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.auth_code.setFont(font)
        self.auth_code.setFrameShadow(QtGui.QFrame.Plain)
        self.auth_code.setScaledContents(True)
        self.auth_code.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.auth_code.setObjectName("auth_code")
        self.authorize_button = QtGui.QPushButton(self.centralwidget)
        self.authorize_button.setGeometry(QtCore.QRect(330, 10, 111, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authorize_button.sizePolicy().hasHeightForWidth())
        self.authorize_button.setSizePolicy(sizePolicy)
        self.authorize_button.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.authorize_button.setFont(font)
        self.authorize_button.setObjectName("authorize_button")
        self.auth_input = QtGui.QLineEdit(self.centralwidget)
        self.auth_input.setGeometry(QtCore.QRect(70, 10, 251, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auth_input.sizePolicy().hasHeightForWidth())
        self.auth_input.setSizePolicy(sizePolicy)
        self.auth_input.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.auth_input.setFont(font)
        self.auth_input.setMouseTracking(False)
        self.auth_input.setAcceptDrops(False)
        self.auth_input.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.auth_input.setReadOnly(False)
        self.auth_input.setObjectName("auth_input")
        self.chat_connect = QtGui.QPushButton(self.centralwidget)
        self.chat_connect.setGeometry(QtCore.QRect(330, 90, 111, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat_connect.sizePolicy().hasHeightForWidth())
        self.chat_connect.setSizePolicy(sizePolicy)
        self.chat_connect.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.chat_connect.setFont(font)
        self.chat_connect.setObjectName("chat_connect")
        self.ads_label = QtGui.QLabel(self.centralwidget)
        self.ads_label.setGeometry(QtCore.QRect(10, 90, 46, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ads_label.sizePolicy().hasHeightForWidth())
        self.ads_label.setSizePolicy(sizePolicy)
        self.ads_label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.ads_label.setFont(font)
        self.ads_label.setFrameShadow(QtGui.QFrame.Plain)
        self.ads_label.setScaledContents(True)
        self.ads_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ads_label.setObjectName("ads_label")
        self.ad_30 = QtGui.QPushButton(self.centralwidget)
        self.ad_30.setEnabled(False)
        self.ad_30.setGeometry(QtCore.QRect(70, 90, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ad_30.sizePolicy().hasHeightForWidth())
        self.ad_30.setSizePolicy(sizePolicy)
        self.ad_30.setSizeIncrement(QtCore.QSize(0, 0))
        self.ad_30.setCheckable(False)
        self.ad_30.setAutoDefault(False)
        self.ad_30.setDefault(False)
        self.ad_30.setFlat(False)
        self.ad_30.setObjectName("ad_30")
        self.ad_60 = QtGui.QPushButton(self.centralwidget)
        self.ad_60.setEnabled(False)
        self.ad_60.setGeometry(QtCore.QRect(110, 90, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ad_60.sizePolicy().hasHeightForWidth())
        self.ad_60.setSizePolicy(sizePolicy)
        self.ad_60.setSizeIncrement(QtCore.QSize(0, 0))
        self.ad_60.setObjectName("ad_60")
        self.ad_150 = QtGui.QPushButton(self.centralwidget)
        self.ad_150.setEnabled(False)
        self.ad_150.setGeometry(QtCore.QRect(230, 90, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ad_150.sizePolicy().hasHeightForWidth())
        self.ad_150.setSizePolicy(sizePolicy)
        self.ad_150.setSizeIncrement(QtCore.QSize(0, 0))
        self.ad_150.setObjectName("ad_150")
        self.ad_120 = QtGui.QPushButton(self.centralwidget)
        self.ad_120.setEnabled(False)
        self.ad_120.setGeometry(QtCore.QRect(190, 90, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ad_120.sizePolicy().hasHeightForWidth())
        self.ad_120.setSizePolicy(sizePolicy)
        self.ad_120.setSizeIncrement(QtCore.QSize(0, 0))
        self.ad_120.setObjectName("ad_120")
        self.ad_90 = QtGui.QPushButton(self.centralwidget)
        self.ad_90.setEnabled(False)
        self.ad_90.setGeometry(QtCore.QRect(150, 90, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ad_90.sizePolicy().hasHeightForWidth())
        self.ad_90.setSizePolicy(sizePolicy)
        self.ad_90.setSizeIncrement(QtCore.QSize(0, 0))
        self.ad_90.setObjectName("ad_90")
        self.ad_180 = QtGui.QPushButton(self.centralwidget)
        self.ad_180.setEnabled(False)
        self.ad_180.setGeometry(QtCore.QRect(270, 90, 31, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ad_180.sizePolicy().hasHeightForWidth())
        self.ad_180.setSizePolicy(sizePolicy)
        self.ad_180.setSizeIncrement(QtCore.QSize(0, 0))
        self.ad_180.setObjectName("ad_180")
        self.title = QtGui.QTextEdit(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(70, 190, 251, 91))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.title.setFont(font)
        self.title.setAcceptRichText(False)
        self.title.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.title.setObjectName("title")
        self.viewer_number = QtGui.QLabel(self.centralwidget)
        self.viewer_number.setGeometry(QtCore.QRect(290, 280, 81, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewer_number.sizePolicy().hasHeightForWidth())
        self.viewer_number.setSizePolicy(sizePolicy)
        self.viewer_number.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setWeight(75)
        font.setBold(True)
        self.viewer_number.setFont(font)
        self.viewer_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.viewer_number.setObjectName("viewer_number")
        self.viewer_peak_text = QtGui.QLabel(self.centralwidget)
        self.viewer_peak_text.setEnabled(True)
        self.viewer_peak_text.setGeometry(QtCore.QRect(70, 330, 211, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewer_peak_text.sizePolicy().hasHeightForWidth())
        self.viewer_peak_text.setSizePolicy(sizePolicy)
        self.viewer_peak_text.setSizeIncrement(QtCore.QSize(0, 0))
        self.viewer_peak_text.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setWeight(75)
        font.setBold(True)
        self.viewer_peak_text.setFont(font)
        self.viewer_peak_text.setFrameShadow(QtGui.QFrame.Plain)
        self.viewer_peak_text.setScaledContents(True)
        self.viewer_peak_text.setAlignment(QtCore.Qt.AlignCenter)
        self.viewer_peak_text.setMargin(0)
        self.viewer_peak_text.setIndent(-1)
        self.viewer_peak_text.setObjectName("viewer_peak_text")
        self.peak_viewer_number = QtGui.QLabel(self.centralwidget)
        self.peak_viewer_number.setGeometry(QtCore.QRect(290, 320, 81, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peak_viewer_number.sizePolicy().hasHeightForWidth())
        self.peak_viewer_number.setSizePolicy(sizePolicy)
        self.peak_viewer_number.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setWeight(75)
        font.setBold(True)
        self.peak_viewer_number.setFont(font)
        self.peak_viewer_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.peak_viewer_number.setObjectName("peak_viewer_number")
        pdt.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(pdt)
        self.statusBar.setObjectName("statusBar")
        pdt.setStatusBar(self.statusBar)

        self.retranslateUi(pdt)
        QtCore.QMetaObject.connectSlotsByName(pdt)
        pdt.setTabOrder(self.auth_input, self.authorize_button)
        pdt.setTabOrder(self.authorize_button, self.nick)
        pdt.setTabOrder(self.nick, self.oauth_get)
        pdt.setTabOrder(self.oauth_get, self.chat_connect)
        pdt.setTabOrder(self.chat_connect, self.ad_30)
        pdt.setTabOrder(self.ad_30, self.ad_60)
        pdt.setTabOrder(self.ad_60, self.ad_90)
        pdt.setTabOrder(self.ad_90, self.ad_120)
        pdt.setTabOrder(self.ad_120, self.ad_150)
        pdt.setTabOrder(self.ad_150, self.ad_180)
        pdt.setTabOrder(self.ad_180, self.game)
        pdt.setTabOrder(self.game, self.title)
        pdt.setTabOrder(self.title, self.update_game_title)
        pdt.setTabOrder(self.update_game_title, self.refresh)
        pdt.setTabOrder(self.refresh, self.chat_send)
        pdt.setTabOrder(self.chat_send, self.send_message)
        pdt.setTabOrder(self.send_message, self.chat_box)

    def retranslateUi(self, pdt):
        pdt.setWindowTitle(QtGui.QApplication.translate("pdt", "PyDash", None, QtGui.QApplication.UnicodeUTF8))
        self.update_game_title.setText(QtGui.QApplication.translate("pdt", "Update Game\n"
"and Title", None, QtGui.QApplication.UnicodeUTF8))
        self.oauth_get.setText(QtGui.QApplication.translate("pdt", "Authorize", None, QtGui.QApplication.UnicodeUTF8))
        self.title_label.setText(QtGui.QApplication.translate("pdt", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.nick_label.setText(QtGui.QApplication.translate("pdt", "Nick:", None, QtGui.QApplication.UnicodeUTF8))
        self.viewer_text.setText(QtGui.QApplication.translate("pdt", "Current Viewers:", None, QtGui.QApplication.UnicodeUTF8))
        self.chat_container.setTitle(QtGui.QApplication.translate("pdt", "Chat", None, QtGui.QApplication.UnicodeUTF8))
        self.send_message.setText(QtGui.QApplication.translate("pdt", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.game_label.setText(QtGui.QApplication.translate("pdt", "Game:", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh.setText(QtGui.QApplication.translate("pdt", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.auth_code.setText(QtGui.QApplication.translate("pdt", "Auth:", None, QtGui.QApplication.UnicodeUTF8))
        self.authorize_button.setText(QtGui.QApplication.translate("pdt", "Get Auth Code", None, QtGui.QApplication.UnicodeUTF8))
        self.chat_connect.setText(QtGui.QApplication.translate("pdt", "Connect to Chat", None, QtGui.QApplication.UnicodeUTF8))
        self.ads_label.setText(QtGui.QApplication.translate("pdt", "Ads:", None, QtGui.QApplication.UnicodeUTF8))
        self.ad_30.setText(QtGui.QApplication.translate("pdt", "30", None, QtGui.QApplication.UnicodeUTF8))
        self.ad_60.setText(QtGui.QApplication.translate("pdt", "60", None, QtGui.QApplication.UnicodeUTF8))
        self.ad_150.setText(QtGui.QApplication.translate("pdt", "150", None, QtGui.QApplication.UnicodeUTF8))
        self.ad_120.setText(QtGui.QApplication.translate("pdt", "120", None, QtGui.QApplication.UnicodeUTF8))
        self.ad_90.setText(QtGui.QApplication.translate("pdt", "90", None, QtGui.QApplication.UnicodeUTF8))
        self.ad_180.setText(QtGui.QApplication.translate("pdt", "180", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setHtml(QtGui.QApplication.translate("pdt", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.viewer_number.setText(QtGui.QApplication.translate("pdt", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.viewer_peak_text.setText(QtGui.QApplication.translate("pdt", "Peak Concurrent:", None, QtGui.QApplication.UnicodeUTF8))
        self.peak_viewer_number.setText(QtGui.QApplication.translate("pdt", "0", None, QtGui.QApplication.UnicodeUTF8))

