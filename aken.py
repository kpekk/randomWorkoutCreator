import sys
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
        self.setWindowIcon(QtGui.QIcon('pics/logo.jpg')) ##mingi norm ikoon vaha leida
        self.setWindowTitle("Trennigenekas")
        self.setStyleSheet(styledef)
        
        self.lihasgrupp1 = QLabel("1.lihasgrupp")
        self.lihasgrupp_valik1 = QComboBox()
        self.lihasgrupp_valik1.addItems(["biits", "triits", "õlad", "core", "selg", "rind", "jalad"])

        self.lihasgrupp2 = QLabel("2.lihasgrupp")
        self.lihasgrupp_valik2 = QComboBox()
        self.lihasgrupp_valik2.addItems(["biits", "triits", "õlad", "core", "selg", "rind", "jalad"])

        self.lihasgrupp3 = QLabel("3.lihasgrupp")
        self.lihasgrupp_valik3 = QComboBox()
        self.lihasgrupp_valik3.addItems(["biits", "triits", "õlad", "core", "selg", "rind", "jalad"])

        #self.lihasgrupp4_opt = ...
        #self.lihasgrupp4 = ...
        #self.lihasgrupp_valik4 = QComboBox()

        self.meil = QLineEdit(self)
        self.meil.setPlaceholderText("meilaadress...")

        self.genereerinupp = QPushButton("davai trenni")

        lay = QGridLayout(self.centralwidget)
        #1.lihasgrupp
        lay.addWidget(self.lihasgrupp1,0,0) 
        self.lihasgrupp1.setStyleSheet(darkstyle)
        lay.addWidget(self.lihasgrupp_valik1,0,1,1,3)
        self.lihasgrupp_valik1.setStyleSheet(darkstyle)
        #2.lihasgrupp
        lay.addWidget(self.lihasgrupp2,1,0)
        self.lihasgrupp2.setStyleSheet(darkstyle)
        lay.addWidget(self.lihasgrupp_valik2,1,1,1,3)
        self.lihasgrupp_valik2.setStyleSheet(darkstyle)
        #3.lihasgrupp
        lay.addWidget(self.lihasgrupp3,2,0)
        self.lihasgrupp3.setStyleSheet(darkstyle)
        lay.addWidget(self.lihasgrupp_valik3,2,1,1,3)
        self.lihasgrupp_valik3.setStyleSheet(darkstyle)
        #optional 4.lihagrupp

        
        lay.addWidget(self.meil,3,1,1,3)
        self.meil.setStyleSheet(darkstyle)
        lay.addWidget(self.genereerinupp,4,1,1,2)
        self.genereerinupp.setStyleSheet(darkstyle)
        self.genereerinupp.clicked.connect(self.genereeri)

        

       
    def genereeri(self):
        lihas1 = self.lihasgrupp_valik1.currentText()
        lihas2 = self.lihasgrupp_valik2.currentText()
        lihas3 = self.lihasgrupp_valik3.currentText()
        meiliaadress = self.meil.text()
        print(meiliaadress)
        treeningkava_main(lihas1, lihas2, lihas3, meiliaadress)
        self.close()
        