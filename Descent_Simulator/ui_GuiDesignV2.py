# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIdesign2CCpVbX.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1001, 850)
        Dialog.setStyleSheet(u"background-color: rgb(74, 75, 72);")
        self.appFrame = QFrame(Dialog)
        self.appFrame.setObjectName(u"appFrame")
        self.appFrame.setGeometry(QRect(0, 0, 1000, 850))
        self.appFrame.setStyleSheet(u"background-color: rgb(54, 55, 56);")
        self.appFrame.setFrameShape(QFrame.StyledPanel)
        self.appFrame.setFrameShadow(QFrame.Raised)
        self.mrtLabel = QLabel(self.appFrame)
        self.mrtLabel.setObjectName(u"mrtLabel")
        self.mrtLabel.setGeometry(QRect(155, -30, 690, 150))
        font = QFont()
        font.setFamily(u"Impact")
        font.setPointSize(42)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mrtLabel.setFont(font)
        self.mrtLabel.setAutoFillBackground(False)
        self.mrtLabel.setStyleSheet(u"font: 42pt \"Impact\";\n"
"color: rgb(207, 28, 22);\n"
"")
        self.inputFrame = QFrame(self.appFrame)
        self.inputFrame.setObjectName(u"inputFrame")
        self.inputFrame.setGeometry(QRect(44, 80, 911, 421))
        self.inputFrame.setStyleSheet(u"background-color: rgb(145, 145, 145);")
        self.inputFrame.setFrameShape(QFrame.StyledPanel)
        self.inputFrame.setFrameShadow(QFrame.Raised)
        self.apogeeLabel = QLabel(self.inputFrame)
        self.apogeeLabel.setObjectName(u"apogeeLabel")
        self.apogeeLabel.setGeometry(QRect(10, 10, 92, 31))
        font1 = QFont()
        font1.setFamily(u"Impact")
        font1.setPointSize(10)
        self.apogeeLabel.setFont(font1)
        self.massLabel = QLabel(self.inputFrame)
        self.massLabel.setObjectName(u"massLabel")
        self.massLabel.setGeometry(QRect(410, 10, 71, 31))
        self.massLabel.setFont(font1)
        self.speedRailLabel = QLabel(self.inputFrame)
        self.speedRailLabel.setObjectName(u"speedRailLabel")
        self.speedRailLabel.setGeometry(QRect(210, 10, 92, 31))
        self.speedRailLabel.setFont(font1)
        self.rocketCSALabel = QLabel(self.inputFrame)
        self.rocketCSALabel.setObjectName(u"rocketCSALabel")
        self.rocketCSALabel.setGeometry(QRect(620, 10, 61, 31))
        self.rocketCSALabel.setFont(font1)
        self.mainAltLabel = QLabel(self.inputFrame)
        self.mainAltLabel.setObjectName(u"mainAltLabel")
        self.mainAltLabel.setGeometry(QRect(10, 240, 121, 31))
        self.mainAltLabel.setFont(font1)
        self.mainParaCSALabel = QLabel(self.inputFrame)
        self.mainParaCSALabel.setObjectName(u"mainParaCSALabel")
        self.mainParaCSALabel.setGeometry(QRect(210, 240, 121, 31))
        self.mainParaCSALabel.setFont(font1)
        self.mainVCDLabel = QLabel(self.inputFrame)
        self.mainVCDLabel.setObjectName(u"mainVCDLabel")
        self.mainVCDLabel.setGeometry(QRect(410, 240, 111, 31))
        self.mainVCDLabel.setFont(font1)
        self.mainTCDLabel = QLabel(self.inputFrame)
        self.mainTCDLabel.setObjectName(u"mainTCDLabel")
        self.mainTCDLabel.setGeometry(QRect(620, 240, 121, 31))
        self.mainTCDLabel.setFont(font1)
        self.longitudeLabel = QLabel(self.inputFrame)
        self.longitudeLabel.setObjectName(u"longitudeLabel")
        self.longitudeLabel.setGeometry(QRect(620, 340, 131, 31))
        self.longitudeLabel.setFont(font1)
        self.windDataLabel = QLabel(self.inputFrame)
        self.windDataLabel.setObjectName(u"windDataLabel")
        self.windDataLabel.setGeometry(QRect(780, 245, 56, 21))
        self.windDataLabel.setFont(font1)
        self.drogueAltInput = QLineEdit(self.inputFrame)
        self.drogueAltInput.setObjectName(u"drogueAltInput")
        self.drogueAltInput.setGeometry(QRect(10, 160, 81, 31))
        font2 = QFont()
        font2.setFamily(u"Impact")
        font2.setPointSize(12)
        self.drogueAltInput.setFont(font2)
        self.drogueAltInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.windDataInput = QLineEdit(self.inputFrame)
        self.windDataInput.setObjectName(u"windDataInput")
        self.windDataInput.setGeometry(QRect(780, 270, 81, 31))
        self.windDataInput.setFont(font2)
        self.windDataInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.massInput = QLineEdit(self.inputFrame)
        self.massInput.setObjectName(u"massInput")
        self.massInput.setGeometry(QRect(410, 40, 81, 31))
        self.massInput.setFont(font2)
        self.massInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.speedInput = QLineEdit(self.inputFrame)
        self.speedInput.setObjectName(u"speedInput")
        self.speedInput.setGeometry(QRect(210, 40, 81, 31))
        self.speedInput.setFont(font2)
        self.speedInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.apogeeInput = QLineEdit(self.inputFrame)
        self.apogeeInput.setObjectName(u"apogeeInput")
        self.apogeeInput.setGeometry(QRect(10, 40, 81, 31))
        self.apogeeInput.setFont(font2)
        self.apogeeInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.mainAltInput = QLineEdit(self.inputFrame)
        self.mainAltInput.setObjectName(u"mainAltInput")
        self.mainAltInput.setGeometry(QRect(10, 270, 81, 31))
        self.mainAltInput.setFont(font2)
        self.mainAltInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.mainParaCSAInput = QLineEdit(self.inputFrame)
        self.mainParaCSAInput.setObjectName(u"mainParaCSAInput")
        self.mainParaCSAInput.setGeometry(QRect(210, 270, 81, 31))
        self.mainParaCSAInput.setFont(font2)
        self.mainParaCSAInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.drogueVCDInput = QLineEdit(self.inputFrame)
        self.drogueVCDInput.setObjectName(u"drogueVCDInput")
        self.drogueVCDInput.setGeometry(QRect(410, 160, 81, 31))
        self.drogueVCDInput.setFont(font2)
        self.drogueVCDInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.mainVCDInput = QLineEdit(self.inputFrame)
        self.mainVCDInput.setObjectName(u"mainVCDInput")
        self.mainVCDInput.setGeometry(QRect(410, 270, 81, 31))
        self.mainVCDInput.setFont(font2)
        self.mainVCDInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.mainTCDInput = QLineEdit(self.inputFrame)
        self.mainTCDInput.setObjectName(u"mainTCDInput")
        self.mainTCDInput.setGeometry(QRect(620, 270, 81, 31))
        self.mainTCDInput.setFont(font2)
        self.mainTCDInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.latitudeInput = QLineEdit(self.inputFrame)
        self.latitudeInput.setObjectName(u"latitudeInput")
        self.latitudeInput.setGeometry(QRect(410, 370, 81, 31))
        self.latitudeInput.setFont(font2)
        self.latitudeInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.drogueTCDInput = QLineEdit(self.inputFrame)
        self.drogueTCDInput.setObjectName(u"drogueTCDInput")
        self.drogueTCDInput.setGeometry(QRect(620, 160, 81, 31))
        self.drogueTCDInput.setFont(font2)
        self.drogueTCDInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rocketCSAInput = QLineEdit(self.inputFrame)
        self.rocketCSAInput.setObjectName(u"rocketCSAInput")
        self.rocketCSAInput.setGeometry(QRect(620, 40, 81, 31))
        self.rocketCSAInput.setFont(font2)
        self.rocketCSAInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.drogueParaCSALabel = QLabel(self.inputFrame)
        self.drogueParaCSALabel.setObjectName(u"drogueParaCSALabel")
        self.drogueParaCSALabel.setGeometry(QRect(210, 130, 121, 31))
        self.drogueParaCSALabel.setFont(font1)
        self.drogueAltLabel = QLabel(self.inputFrame)
        self.drogueAltLabel.setObjectName(u"drogueAltLabel")
        self.drogueAltLabel.setGeometry(QRect(10, 130, 131, 31))
        self.drogueAltLabel.setFont(font1)
        self.drogueParaCSAInput = QLineEdit(self.inputFrame)
        self.drogueParaCSAInput.setObjectName(u"drogueParaCSAInput")
        self.drogueParaCSAInput.setGeometry(QRect(210, 160, 81, 31))
        self.drogueParaCSAInput.setFont(font2)
        self.drogueParaCSAInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.drogueVCDLabel = QLabel(self.inputFrame)
        self.drogueVCDLabel.setObjectName(u"drogueVCDLabel")
        self.drogueVCDLabel.setGeometry(QRect(410, 130, 111, 31))
        self.drogueVCDLabel.setFont(font1)
        self.drogueTCDLabel = QLabel(self.inputFrame)
        self.drogueTCDLabel.setObjectName(u"drogueTCDLabel")
        self.drogueTCDLabel.setGeometry(QRect(620, 130, 121, 31))
        self.drogueTCDLabel.setFont(font1)
        self.zenithLabel = QLabel(self.inputFrame)
        self.zenithLabel.setObjectName(u"zenithLabel")
        self.zenithLabel.setGeometry(QRect(10, 340, 71, 31))
        self.zenithLabel.setFont(font1)
        self.zenithInput = QLineEdit(self.inputFrame)
        self.zenithInput.setObjectName(u"zenithInput")
        self.zenithInput.setGeometry(QRect(10, 370, 81, 31))
        self.zenithInput.setFont(font2)
        self.zenithInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.azimuthLabel = QLabel(self.inputFrame)
        self.azimuthLabel.setObjectName(u"azimuthLabel")
        self.azimuthLabel.setGeometry(QRect(210, 340, 81, 31))
        self.azimuthLabel.setFont(font1)
        self.azimuthInput = QLineEdit(self.inputFrame)
        self.azimuthInput.setObjectName(u"azimuthInput")
        self.azimuthInput.setGeometry(QRect(210, 370, 81, 31))
        self.azimuthInput.setFont(font2)
        self.azimuthInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.latitudeLabel = QLabel(self.inputFrame)
        self.latitudeLabel.setObjectName(u"latitudeLabel")
        self.latitudeLabel.setGeometry(QRect(410, 340, 91, 31))
        self.latitudeLabel.setFont(font1)
        self.longitudeInput = QLineEdit(self.inputFrame)
        self.longitudeInput.setObjectName(u"longitudeInput")
        self.longitudeInput.setGeometry(QRect(620, 370, 81, 31))
        self.longitudeInput.setFont(font2)
        self.longitudeInput.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.simulationLabel = QLabel(self.inputFrame)
        self.simulationLabel.setObjectName(u"simulationLabel")
        self.simulationLabel.setGeometry(QRect(780, 340, 125, 31))
        font3 = QFont()
        font3.setFamily(u"Impact")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.simulationLabel.setFont(font3)
        self.simulationLabel.setStyleSheet(u"\n"
"font: 10pt \"Impact\";")
        self.simulationInput_7 = QLineEdit(self.inputFrame)
        self.simulationInput_7.setObjectName(u"simulationInput_7")
        self.simulationInput_7.setGeometry(QRect(780, 370, 81, 31))
        self.simulationInput_7.setFont(font2)
        self.simulationInput_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.circularFrame = QFrame(self.appFrame)
        self.circularFrame.setObjectName(u"circularFrame")
        self.circularFrame.setGeometry(QRect(260, 510, 461, 311))
        self.circularFrame.setFrameShape(QFrame.StyledPanel)
        self.circularFrame.setFrameShadow(QFrame.Raised)
        self.ProgressBarFrame = QFrame(self.circularFrame)
        self.ProgressBarFrame.setObjectName(u"ProgressBarFrame")
        self.ProgressBarFrame.setGeometry(QRect(70, 0, 320, 320))
        self.ProgressBarFrame.setStyleSheet(u"")
        self.ProgressBarFrame.setFrameShape(QFrame.NoFrame)
        self.ProgressBarFrame.setFrameShadow(QFrame.Raised)
        self.circularProgressBar = QFrame(self.ProgressBarFrame)
        self.circularProgressBar.setObjectName(u"circularProgressBar")
        self.circularProgressBar.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgressBar.setStyleSheet(u"QFrame{\n"
"	\n"
"	border-radius: 150px;\n"
"	\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(0, 0, 0, 0), stop:0.750 rgba(150, 0, 20, 255));\n"
"\n"
"\n"
"}")
        self.circularProgressBar.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBar)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(20, 20, 260, 260))
        self.container.setStyleSheet(u"QFrame{\n"
"\n"
"	border-radius: 130px;\n"
"	background-color: rgb(54, 55, 56);\n"
"\n"
"}\n"
"")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.Percent_Label = QLabel(self.container)
        self.Percent_Label.setObjectName(u"Percent_Label")
        self.Percent_Label.setGeometry(QRect(70, 70, 131, 101))
        font4 = QFont()
        font4.setFamily(u"Impact")
        font4.setPointSize(60)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setWeight(50)
        self.Percent_Label.setFont(font4)
        self.Percent_Label.setStyleSheet(u"background-color: none;\n"
"color: #FFFFFF")
        self.Percent_Label.setAlignment(Qt.AlignCenter)
        self.circularBG = QFrame(self.ProgressBarFrame)
        self.circularBG.setObjectName(u"circularBG")
        self.circularBG.setGeometry(QRect(10, 10, 300, 300))
        self.circularBG.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: rgba(255,255, 255, 110);\n"
"}")
        self.circularBG.setFrameShape(QFrame.NoFrame)
        self.circularBG.setFrameShadow(QFrame.Raised)
        self.circularBG.raise_()
        self.circularProgressBar.raise_()
        self.launchButton = QPushButton(self.appFrame)
        self.launchButton.setObjectName(u"launchButton")
        self.launchButton.setGeometry(QRect(720, 630, 201, 91))
        font5 = QFont()
        font5.setFamily(u"Impact")
        font5.setPointSize(20)
        self.launchButton.setFont(font5)
        self.launchButton.setStyleSheet(u"color: rgb(207, 28, 22);\n"
"border-color: rgb(255, 0, 0);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.mrtLabel.setText(QCoreApplication.translate("Dialog", u"McGill Rocket Team Simulator", None))
        self.apogeeLabel.setText(QCoreApplication.translate("Dialog", u"Expected Apogee", None))
        self.massLabel.setText(QCoreApplication.translate("Dialog", u"Rocket Mass", None))
        self.speedRailLabel.setText(QCoreApplication.translate("Dialog", u"Speed Off Raill", None))
        self.rocketCSALabel.setText(QCoreApplication.translate("Dialog", u"Rocket CSA", None))
        self.mainAltLabel.setText(QCoreApplication.translate("Dialog", u"Main Deploy Altitude", None))
        self.mainParaCSALabel.setText(QCoreApplication.translate("Dialog", u"Main Parachute CSA", None))
        self.mainVCDLabel.setText(QCoreApplication.translate("Dialog", u"Main Vertical Cd", None))
        self.mainTCDLabel.setText(QCoreApplication.translate("Dialog", u"Main Transverse Cd", None))
        self.longitudeLabel.setText(QCoreApplication.translate("Dialog", u"Launch Longitude", None))
        self.windDataLabel.setText(QCoreApplication.translate("Dialog", u"Wind Data", None))
        self.drogueParaCSALabel.setText(QCoreApplication.translate("Dialog", u"Drogue Parachute CSA", None))
        self.drogueAltLabel.setText(QCoreApplication.translate("Dialog", u"Drogue Deploy Altitude", None))
        self.drogueVCDLabel.setText(QCoreApplication.translate("Dialog", u"Drogue Vertical Cd", None))
        self.drogueTCDLabel.setText(QCoreApplication.translate("Dialog", u"Drogue Transverse Cd", None))
        self.zenithLabel.setText(QCoreApplication.translate("Dialog", u"Zenith Angle", None))
        self.azimuthLabel.setText(QCoreApplication.translate("Dialog", u"Azimuth Angle", None))
        self.latitudeLabel.setText(QCoreApplication.translate("Dialog", u"Launch Latitude", None))
        self.simulationLabel.setText(QCoreApplication.translate("Dialog", u"Number of Simulations", None))
        self.Percent_Label.setText(QCoreApplication.translate("Dialog", u"<p><span style=\" font-size:68pt;\">0</span><span style=\" font-size:48pt; vertical-align:super;\">%</span></p>", None))
        self.launchButton.setText(QCoreApplication.translate("Dialog", u"Launch", None))
    # retranslateUi

