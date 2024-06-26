from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, QRunnable, QThreadPool
from PyQt5.QtWidgets import QCompleter
import requests
import json
import geocoder
from src.map import MapWindow
import ast

class Communicator(QObject):
    coordinates_signal = pyqtSignal(int) 

class Ui_BuyerWindow(object):

    def __init__(self):
        self.config = json.load(open("src/config.json", 'r'))
        self.allpincodes = requests.get(self.config["GetMerchants"]).text
        try:
            self.numbers = ast.literal_eval(self.allpincodes)
            if not isinstance(self.numbers, list):
                raise ValueError("Input string is not a list")
        except (ValueError, SyntaxError) as e:
            print(f"Error parsing input list: {e}")
            return

        str_numbers = list(map(str, self.numbers))
        self.completer = QCompleter(str_numbers)
        self.threadpool = QThreadPool()
        print(f"Multithreading with maximum {self.threadpool.maxThreadCount()} threads")


    def setupUi(self, MainWindow):
        self.activated = 'pincodes'
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1536, 864)
        MainWindow.setMinimumSize(QtCore.QSize(1536, 864))
        MainWindow.setMaximumSize(QtCore.QSize(1536, 864))
        MainWindow.setStyleSheet("background-color :#e8e8e8;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Assets/logo2.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1340, 800, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#3f3f3f;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1406, 800, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#4285F4;")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 20, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"border-radius:25;\n"
"border: 3px solid #0085ff;\n"
"border-color:#0085ffsu;\n"
"background:transparent;\n"
"color:#3f3f3f;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"border-radius:25;\n"
"border: 3px solid #75A9FF;\n"
"border-color:#0085ffsu;\n"
"background-color:#75A9FF\n"
"}\n"
"\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/b2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 129, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"border-radius:25;\n"
"border: 3px solid #0085ff;\n"
"border-color:#0085ffsu;\n"
"background:transparent;\n"
"color:#3f3f3f;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover{\n"
"border-radius:25;\n"
"border: 3px solid #75A9FF;\n"
"border-color:#0085ffsu;\n"
"background-color:#75A9FF\n"
"}\n"
"\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Assets/marker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(214, 130, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
"border-radius:25;\n"
"border: 3px solid #0085ff;\n"
"border-color:#0085ffsu;\n"
"background:transparent;\n"
"color:#3f3f3f;\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover{\n"
"border-radius:25;\n"
"border: 3px solid #75A9FF;\n"
"border-color:#0085ffsu;\n"
"background-color:#75A9FF\n"
"}\n"
"\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Assets/gpa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 130, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
"border-radius:25;\n"
"border: 3px solid #0085ff;\n"
"border-color:#0085ffsu;\n"
"background:transparent;\n"
"color:#3f3f3f;\n"
"}\n"
"\n"
"QPushButton#pushButton_4:hover{\n"
"border-radius:25;\n"
"border: 3px solid #75A9FF;\n"
"border-color:#0085ffsu;\n"
"background-color:#75A9FF\n"
"}\n"
"\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Assets/current-location-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(980, 140, 451, 611))
        self.scrollArea.setStyleSheet("background-color:#e2e2e2;\n"
"border-radius:25")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 437, 611))
        self.scrollAreaWidgetContents.setBaseSize(QtCore.QSize(300, 300))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(30, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 620, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_5{\n"
"border-radius:25;\n"
"border: 3px solid #0085ff;\n"
"border-color:#0085ffsu;\n"
"background-color:#4285F4;\n"
"color:#1f1f1f;\n"
"}\n"
"\n"
"QPushButton#pushButton_5:hover{\n"
"border-radius:25;\n"
"border: 3px solid #75A9FF;\n"
"border-color:#0085ffsu;\n"
"background-color:#75A9FF\n"
"}\n"
"\n"
"\n"
"r")
        self.pushButton_5.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pincodes = QtWidgets.QFrame(self.centralwidget)
        self.pincodes.setGeometry(QtCore.QRect(40, 200, 821, 411))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        self.pincodes.setFont(font)
        self.pincodes.setStyleSheet("border:0")
        self.pincodes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pincodes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pincodes.setObjectName("pincodes")
        self.label_6 = QtWidgets.QLabel(self.pincodes)
        self.label_6.setGeometry(QtCore.QRect(40, 50, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:black;")
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.pincodes)
        self.pushButton_6.setGeometry(QtCore.QRect(650, 90, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton#pushButton_6{\n"
"border-radius:21;\n"
"background-color:#4285F4;\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton#pushButton_6:hover{\n"
"border-radius:21;\n"
"background-color:#75A9FF;\n"
"color:black;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_11 = QtWidgets.QLabel(self.pincodes)
        self.label_11.setGeometry(QtCore.QRect(60, 140, 531, 21))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:#6a6a6a;background:transparent;")
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(self.pincodes)
        self.lineEdit.setGeometry(QtCore.QRect(70, 100, 541, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.frame = QtWidgets.QFrame(self.pincodes)
        self.frame.setGeometry(QtCore.QRect(40, 90, 600, 50))
        self.frame.setStyleSheet("border-radius:25;\n"
"border: 3px solid #0085ff;\n"
"border-color:#0085ffsu;\n"
"background:transparent;\n"
"color:black;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6.raise_()
        self.pushButton_6.raise_()
        self.label_11.raise_()
        self.frame.raise_()
        self.lineEdit.raise_()
        self.gps = QtWidgets.QFrame(self.centralwidget)
        self.gps.setGeometry(QtCore.QRect(40, 200, 821, 411))
        self.gps.setStyleSheet("border:0;")
        self.gps.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gps.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gps.setObjectName("gps")
        self.textEdit_2 = QtWidgets.QTextEdit(self.gps)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 90, 651, 51))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("border-radius:25;\n"
"border: 3px solid #0085ff;\n"
"border-color:#0085ffsu;\n"
"background:transparent;\n"
"color:black;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_7 = QtWidgets.QLabel(self.gps)
        self.label_7.setGeometry(QtCore.QRect(40, 50, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:black;")
        self.label_7.setObjectName("label_7")
        self.textEdit_3 = QtWidgets.QTextEdit(self.gps)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 210, 651, 51))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("border-radius:25;\n"
"border: 3px solid #0085ff;\n"
"border-color:#0085ffsu;\n"
"background:transparent;\n"
"color:black;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_8 = QtWidgets.QLabel(self.gps)
        self.label_8.setGeometry(QtCore.QRect(40, 170, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:black;")
        self.label_8.setObjectName("label_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.gps)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 280, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton#pushButton_7{\n"
"border-radius:15;\n"
"background-color:#4285F4;\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton#pushButton_7:hover{\n"
"border-radius:15;\n"
"background-color:#75A9FF;\n"
"color:black;\n"
"}\n"
"\n"
"\n"
"r")
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.location = QtWidgets.QFrame(self.centralwidget)
        self.location.setGeometry(QtCore.QRect(40, 200, 821, 411))
        self.location.setStyleSheet("border:0")
        self.location.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.location.setFrameShadow(QtWidgets.QFrame.Raised)
        self.location.setObjectName("location")
        self.textEdit_4 = QtWidgets.QTextEdit(self.location)
        self.textEdit_4.setGeometry(QtCore.QRect(40, 90, 651, 51))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("border-radius:25;\n"
"border: 3px solid #0085ff;\n"
"border-color:#0085ffsu;\n"
"background:transparent;\n"
"color:black;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_9 = QtWidgets.QLabel(self.location)
        self.label_9.setGeometry(QtCore.QRect(40, 50, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:black;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.location)
        self.label_10.setGeometry(QtCore.QRect(60, 140, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:#6a6a6a;background : transparent;")
        self.label_10.setObjectName("label_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(500, 130, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton#pushButton_8{\n"
"border-radius:25;\n"
"border: 3px solid #0085ff;\n"
"border-color:#0085ffsu;\n"
"background:transparent;\n"
"color:#3f3f3f;\n"
"}\n"
"\n"
"QPushButton#pushButton_8:hover{\n"
"border-radius:25;\n"
"border: 3px solid #75A9FF;\n"
"border-color:#0085ffsu;\n"
"background-color:#75A9FF\n"
"}\n"
"\n"
"\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Assets/shop2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon4)
        self.pushButton_8.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_8.setObjectName("pushButton_8")
        self.merchants = QtWidgets.QFrame(self.centralwidget)
        self.merchants.setGeometry(QtCore.QRect(40, 200, 821, 411))
        self.merchants.setStyleSheet("border:0;")
        self.merchants.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.merchants.setFrameShadow(QtWidgets.QFrame.Raised)
        self.merchants.setObjectName("merchants")
        self.frame_2 = QtWidgets.QFrame(self.merchants)
        self.frame_2.setGeometry(QtCore.QRect(40, 90, 600, 50))
        self.frame_2.setStyleSheet("border-radius:25;\n"
"border: 3px solid #0085ff;\n"
"border-color:#0085ffsu;\n"
"background:transparent;\n"
"color:black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.merchants)
        self.label_4.setGeometry(QtCore.QRect(40, 50, 341, 30))
        font = QtGui.QFont()
        font.setFamily("Google Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.merchants)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 103, 540, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.scrollArea.raise_()
        self.pushButton_5.raise_()
        self.pushButton_3.raise_()
        self.pushButton_8.raise_()
        self.gps.raise_()
        self.location.raise_()
        self.pincodes.raise_()
        self.merchants.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.communicator = Communicator()
        self.communicator.coordinates_signal.connect(self.update_coordinates)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Team Creovate"))
        self.label_2.setText(_translate("MainWindow", "Team"))
        self.label_3.setText(_translate("MainWindow", "Creovate"))
        self.pushButton.setText(_translate("MainWindow", "    Buyer"))
        self.pushButton_2.setText(_translate("MainWindow", "    Pincodes"))
        self.pushButton_3.setText(_translate("MainWindow", "   GPS"))
        self.pushButton_4.setText(_translate("MainWindow", "   Location"))
        self.pushButton_5.setText(_translate("MainWindow", "SEARCH"))
        self.label_6.setText(_translate("MainWindow", "Enter Pincode(s)"))
        self.pushButton_6.setText(_translate("MainWindow", "   Open Map"))
        self.label_11.setText(_translate("MainWindow", "Enter multiple pincodes separated by commas e.g., 110001,500001,201301"))
        self.label_7.setText(_translate("MainWindow", "Enter Latitude"))
        self.label_8.setText(_translate("MainWindow", "Enter Longitude"))
        self.pushButton_7.setText(_translate("MainWindow", "   Get Current Location"))
        self.label_9.setText(_translate("MainWindow", "Enter Location Name"))
        self.label_10.setText(_translate("MainWindow", "Enter multiple locations separated by commas e.g., Delhi,Bengaluru"))
        self.pushButton_8.setText(_translate("MainWindow", "  Merchants"))
        self.label_4.setText(_translate("MainWindow", "Enter Merchant Name"))


        self.lineEdit.setCompleter(self.completer)

        
        self.pushButton_2.clicked.connect(lambda :self.changeMode(self.pincodes,self.gps,self.location,self.merchants,'pincodes'))

        self.pushButton_3.clicked.connect(lambda :self.changeMode(self.gps,self.pincodes,self.location,self.merchants,'gps'))

        self.pushButton_4.clicked.connect(lambda: self.changeMode(self.location,self.gps,self.pincodes,self.merchants,'location'))

        self.pushButton_8.clicked.connect(lambda: self.changeMode(self.merchants,self.gps,self.pincodes,self.location,'merchants'))
        self.pushButton_6.clicked.connect(lambda: self.open_map_view())
        self.pushButton_5.clicked.connect(lambda: self.SendReq(self.activated))
        self.pushButton_7.clicked.connect(lambda: self.get_current_location())

        self.location.hide()
        self.merchants.hide()
        self.gps.hide()

    def addUi(self, x):

        for i in reversed(range(self.verticalLayout_2.count())):
            self.verticalLayout_2.itemAt(i).widget().setParent(None)

        if len(x) == 1 and x[0] == "Null":
            x[0] = "No Merchants found"
        for i in range(len(x)):
            self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            self.frame.setMinimumSize(QtCore.QSize(360, 55))
            self.frame.setMaximumSize(QtCore.QSize(360, 55))
            self.frame.setStyleSheet("background-color:#4285F4;color:black;")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame_" + str(i))
            self.label_4 = QtWidgets.QLabel(self.frame)
            self.label_4.setGeometry(QtCore.QRect(40, 0, 271, 51))
            font = QtGui.QFont()
            font.setFamily("Google Sans")
            font.setBold(True)
            font.setWeight(75)
            self.label_4.setFont(font)
            self.label_4.setStyleSheet("color:white")
            self.label_4.setObjectName("label_4_" + str(i))
            self.label_4.setText(x[i])
            self.verticalLayout_2.addWidget(self.frame)

    def UpdateMerchants(self, data):
        for i in range(len(data)):
            self.addUi(data[i])

    def changeMode(self, active, nactive, nactive2, nactive3, activated):
        self.activated = activated
        active.show()
        nactive.hide()
        nactive2.hide()
        nactive3.hide()

    def SendReq(self, mode):
        print(mode)
        if mode == 'pincodes':
            rawTxt = self.lineEdit.text()
            data = rawTxt
        elif mode == 'gps':
            data = self.textEdit_2.toPlainText() + ',' + self.textEdit_3.toPlainText()
        elif mode == 'location':
            data = self.textEdit_4.toPlainText()
        elif mode == 'merchants':
            data = self.lineEdit_2.text()

        worker = RequestWorker(self.config, mode, data)
        worker.signals.result.connect(self.addUi)
        worker.signals.error.connect(self.displayError)
        self.threadpool.start(worker)

    def displayError(self, error):
        print(f"Error: {error}")

    def update_coordinates(self, x):
        print('started', x)
        if len(str(x)) == 6:
            oldtxt = self.lineEdit.text()
            if len(oldtxt) == 0:
                self.lineEdit.setText(str(x) + ',')
            elif oldtxt[-1] == ',':
                self.lineEdit.setText(oldtxt + str(x) + ',')
        else:
            print("Pincode not found")

    def open_map_view(self):
        self.map_window = MapWindow()
        self.map_window.bridge.coordinates_received.connect(self.communicator.coordinates_signal.emit)
        self.map_window.show()

    def get_current_location(self):
        g = geocoder.ip('me')

        if g.ok:
            latitude = g.latlng[0]
            longitude = g.latlng[1]
            print(latitude, longitude)
            self.textEdit_2.setText(str(latitude))
            self.textEdit_3.setText(str(longitude))

class RequestWorkerSignals(QObject):
    result = pyqtSignal(list)
    error = pyqtSignal(str)

class RequestWorker(QRunnable):
    def __init__(self, config, mode, data):
        super(RequestWorker, self).__init__()
        self.config = config
        self.mode = mode
        self.data = data
        self.signals = RequestWorkerSignals()

    def run(self):
        try:
            if self.mode == 'merchants':
                params = {'merchant': self.data}
                response = requests.get(self.config["MerchantQuery"], params=params)
                print(response.text)
                master_data = response.text.split(":")[1].split(",")
                new_master_data = [i.strip() for i in master_data if i.strip() != "No Merchants Found" or i.strip() != 'Null']
                self.signals.result.emit(new_master_data)
            else:
                
                params = {'data': self.data, 'mode': self.mode}
                print(params,self.mode)
                response = requests.get(self.config['BuyerAPI'], params=params)
                master_data = response.text.split(",")
                print(master_data)
                new_master_data = [i.strip() for i in master_data if i.strip() != "No Merchants Found"]
                new_master_data = [i.strip() for i in master_data if i.strip() != 'Null']
                self.signals.result.emit(new_master_data)
        except Exception as e:
            self.signals.error.emit(str(e))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_BuyerWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())