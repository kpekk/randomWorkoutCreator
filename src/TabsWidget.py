from PyQt5.QtWidgets import *
from WorkOutTab import WorkOutTab
from SettingsTab import SettingsTab

class TabsWidget(QWidget):
    def __init__(self, parent):
        
        super(QWidget, self).__init__(parent)
        self.tabs = QTabWidget()
        
        #Workout tab
        self.tab1 = WorkOutTab(self)
        self.tabs.addTab(self.tab1,"Workout")

        #Settings tab
        self.tab2 = SettingsTab(self)
        self.tabs.addTab(self.tab2,"Settings")

        #refresh excercise selection on tab change
        self.tabs.currentChanged.connect(self.callChange)

        # Add tabs to widget
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def callChange(self):
        self.tab1.getExercises()

