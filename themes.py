from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


QApplication.setStyle("Fusion") #ülejäänud themed koledad

darkstyle = """
QPushButton{
    background-color:rgb(53,53,53); color:red; border-style: outset; border-width: 4px; border-color: rgb(53,53,53) 
}
QPushButton:pressed{
    background-color:gray;   
}
QLabel{
    background-color:rgb(53,53,53); color:red;
}
QLineEdit{
    background-color:rgb(53,53,53); color:red;
    
}
QComboBox{
    background-color:rgb(228,77,218);
}
"""
styledef = """
Algaken {
    background-color: rgb(57,57,57);
}
"""

