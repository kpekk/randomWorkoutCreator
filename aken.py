import sys
import re
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5 import QtGui, QtCore, QtWidgets
from themes import *
from treeningkava_main import *
class Algaken(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640,440)
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        #set stylesheet
        self.setStyleSheet(darkstyle)

        #removes title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #Layout (aka the main widget)
        lay = QGridLayout(self.centralwidget)

        #All possible options
        predef = ["Biceps", "Triceps", "Shoulders", "Core", "Back", "Chest", "Legs"]

        #Close button
        self.exitButton = QPushButton("Close")
        lay.addWidget(self.exitButton,4,3,1,1)
        self.exitButton.clicked.connect(self.close)

        #1st muscle group
        lay.addWidget(QLabel("Muscle group #1"),0,0)
        self.option1 = QComboBox()
        self.option1.addItems(predef) 
        lay.addWidget(self.option1,0,1,1,3)

        #2nd muscle group
        lay.addWidget(QLabel("Muscle group #2"),1,0)
        self.option2 = QComboBox()
        self.option2.addItems(predef)
        lay.addWidget(self.option2,1,1,1,3)

        #3rd muscle group
        lay.addWidget(QLabel("Muscle group #3"),2,0)
        self.option3 = QComboBox()
        self.option3.addItems(predef)
        lay.addWidget(self.option3,2,1,1,3)

        #mail address
        self.mailAddress = QLineEdit(self)
        self.mailAddress.setPlaceholderText("Mail address")
        self.mailAddress.textChanged.connect(self.validateEmail)
        lay.addWidget(self.mailAddress,3,0,1,4)

        #generate button
        self.generateButton = QPushButton("Enter valid email")
        lay.addWidget(self.generateButton,4,1,1,2)
        self.generateButton.clicked.connect(self.generate)
        #inactive if mail address field is empty
        self.generateButton.setDisabled(True)

    def exitOnClick(self):
        self.close()

    #Validate email
    def validateEmail(self):
        text = self.mailAddress.text()
        if re.match(r"[^@]+@[^@]+\.[^@]+", text):
            self.generateButton.setDisabled(False)
            self.generateButton.setText("I'm ready, hit it!")
        else:
            self.generateButton.setDisabled(True)
            self.generateButton.setText("Enter valid email")

    def generate(self):
        lihas1 = self.option1.currentText()
        lihas2 = self.option2.currentText()
        lihas3 = self.option3.currentText()
        mail = self.mailAddress.text()

        treeningkava_main(lihas1, lihas2, lihas3, mail)
        #self.close()
        