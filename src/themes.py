from PyQt5.QtWidgets import QApplication

#fusion just looks better than the other styles
QApplication.setStyle("Fusion")

darkstyle = """
QWidget{
    /*Will be overriden if defined below*/
    background-color: rgb(57,57,57);
    color: red;
}
QRadioButton {
    color:                  white;
}
QRadioButton::indicator {
    width:                  10px;
    height:                 10px;
    border-radius:          7px;
}
QRadioButton::indicator:checked {
    background-color:       red;
    border:                 2px solid white;
}
QRadioButton::indicator:unchecked {
    background-color:       gray;
    border:                 2px solid white;
}
QCheckBox{
border: 1px solid red;
}
QPushButton{
    background-color:rgb(53,53,53); 
    color:red; 
    border-style: outset; 
    border-width: 4px; 
    border-color: rgb(53,53,53); 
}
QPushButton:pressed{
    background-color:gray;   
}
QPushButton:disabled{
    background-color:rgb(255,87,87); 
    color: black;  
}
QLabel{
    background-color:rgb(53,53,53); color:red;
}

QLineEdit{
    background-color:rgb(50,50,50); color:red;
}
QLineEdit:disabled{
    background-color:rgb(43,43,43);
}

QComboBox{
    color:red;
}
QComboBox:disabled{
    background-color: rgb(43,43,43);
}

QComboBox QAbstractItemView
{
    background-color: gray;
}
MainWindow {
    background-color: rgb(57,57,57);
    border: 3px solid red;
}
"""
