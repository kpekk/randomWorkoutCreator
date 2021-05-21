from PyQt5.QtWidgets import *
from themes import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,800)

        #stylesheet
        self.setStyleSheet(darkstyle)

        #tabswidget for switching tabs
        self.centralwidget = TabsWidget(self)
        self.setCentralWidget(self.centralwidget)

        #removes the title bar (the user can't move the app, not recommended)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.show()
       

#avoiding circular depencencies 'n stuff by moving these two here
from WorkOutTab import *
from TabsWidget import TabsWidget