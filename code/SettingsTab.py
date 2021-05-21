import os, re
from PyQt5.QtWidgets import *
from themes import *
from treeningkava_main import *
import subprocess

class SettingsTab(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        # Layout (aka the main widget)
        lay = QGridLayout(self)
        
        #Validate email
        def validateEmail():
            text = self.testAddressField.text()
            if re.match(r"[^@]+@[^@]+\.[^@]+", text):
                self.testButton.setDisabled(False)
                self.testButton.setText("Send")
            else:
                self.testButton.setDisabled(True)

        #send a test email
        def sendTestEmail():
            treeningkava_main("testEmail","",0, self.testAddressField.text())

        #updating sender email address label
        def updateSenderEmailLabel():
            sender_email = ""
            with open("config\email.txt", "r+") as f:
                sender_email = f.read().split("\n")

            sender_email = sender_email[0].strip()

            if sender_email == "":
                sender_email = "No suitable email found!"
            self.senderEmail.setText(sender_email)

        #changing sender email address
        def changeSenderEmail():
            #open notepad to change info
            p = subprocess.call(["notepad.exe", "config/email.txt"])

            #update email label (will be done once the notepad is closed)
            updateSenderEmailLabel()

        #changing the size of the sample chosen from an excercise group
        def changeSampleSize():
            with open("config\sample_size.txt","w+") as f:
                f.write(self.sampleSizeTextField.text())

        def updateSampleSize():
            sample_size = ""
            with open("config\sample_size.txt", "r+") as f:
                sample_size = f.read().strip()

            if sample_size == "":
                sample_size = "3"
            self.sampleSizeTextField.setText(sample_size)


#--------modifying excercises

    #---edit excercise
        # label & radiobutton
        self.editLabel = QLabel("Edit exercise")
        self.editExisting = QRadioButton()
        self.editExisting.setChecked(True)  # default choice
        lay.addWidget(self.editLabel, 0, 0, 1, 1)
        lay.addWidget(self.editExisting, 0, 1, 1, 1)

        # the excercise selection
        self.editMenu = QComboBox()
        lay.addWidget(self.editMenu, 0, 2, 1, 2)

    #---add new excercise
        # 'new excercise' label
        self.addNew = QRadioButton()
        self.addLabel = QLabel("Add new exercise")
        lay.addWidget(self.addLabel, 1, 0, 1, 1)
        lay.addWidget(self.addNew, 1, 1, 1, 1)

        # the 'new excercise' field
        self.newExercise = QLineEdit()
        self.newExercise.setPlaceholderText("New exercise name...")
        self.newExercise.setDisabled(True)
        lay.addWidget(self.newExercise, 1, 2, 1, 2)

    #---delete excercise
        self.delete = QRadioButton()
        self.deleteLabel = QLabel("Delete exercise")
        lay.addWidget(self.deleteLabel, 2, 0, 1, 1)
        lay.addWidget(self.delete, 2, 1, 1, 1)

        # the excercise selection
        self.deleteMenu = QComboBox()
        self.deleteMenu.setDisabled(True)
        lay.addWidget(self.deleteMenu, 2, 2, 1, 2)

    #---execute chosen command
        # file edit button
        self.editButton = QPushButton("Edit exercise")
        lay.addWidget(self.editButton, 3, 1, 1, 2)
        self.editButton.clicked.connect(self.pickAction)

        #connect mode changing to radiobutton changes
        self.editExisting.toggled.connect(self.changeMode)
        self.addNew.toggled.connect(self.changeMode)
        self.delete.toggled.connect(self.changeMode)

    #---changing subexcercise count
        lay.addWidget(QLabel("Exercise sample size"),4,0,1,1)
        self.sampleSizeTextField = QLineEdit("3") #3 by default
        self.changeSampleSizeButton = QPushButton("Update")
        self.changeSampleSizeButton.clicked.connect(changeSampleSize)

        lay.addWidget(self.sampleSizeTextField,4,1,1,2)
        lay.addWidget(self.changeSampleSizeButton,4,3,1,1)

        updateSampleSize() #loading the sample size from 'sample_size.txt'

    #---update available excercises
        self.getExercises()

#--------configuring sender email

        self.currentLabel = QLabel("Current sender email: ")
        lay.addWidget(self.currentLabel,5,0,1,1)

        #sender email address label
        self.senderEmail = QLabel()
        updateSenderEmailLabel()
        lay.addWidget(self.senderEmail,5,1,1,2)

        #sender email & password config button
        self.configButton = QPushButton("Change") 
        lay.addWidget(self.configButton,5,3,1,1)   
        self.configButton.clicked.connect(changeSenderEmail)

#--------sending a test email

        #email address label
        self.testLabel = QLabel("Send a test email to: ")
        lay.addWidget(self.testLabel,6,0,1,1)

        #email address field
        self.testAddressField = QLineEdit(self)
        self.testAddressField.setPlaceholderText("Email address")
        self.testAddressField.textChanged.connect(validateEmail)
        lay.addWidget(self.testAddressField,6,1,1,2)  

        #email address submit button
        self.testButton = QPushButton("Send") 
        lay.addWidget(self.testButton,6,3,1,1)   
        self.testButton.clicked.connect(sendTestEmail)
        self.testButton.setDisabled(True)

##other functions

    #change the currently active mode (delete/add/modify excercise)
    def changeMode(self):
        #disable all options by default
        self.editMenu.setDisabled(True)
        self.deleteMenu.setDisabled(True)
        self.newExercise.setDisabled(True)

        #'edit excercise' mode selected
        if(self.editExisting.isChecked()):
            #enable self
            self.editMenu.setDisabled(False)
            self.editButton.setText("Edit exercise")
        
        #'add excercise' mode selected
        elif (self.addNew.isChecked()):
            #enable self
            self.newExercise.setDisabled(False)
            self.editButton.setText("Add exercise")
        
        #'delete excercise' mode selected
        else:
            self.deleteMenu.setDisabled(False)
            self.editButton.setText("Delete exercise")

    #refresh excercise list
    def getExercises(self):
        # get all user-defined excercises
        if os.path.exists("resources/exercises/"):
            files = os.listdir("resources/exercises/")
            options = []
            for file in files:
                options.append(file.replace(".txt", ""))

            #refresh comboboxes
            for i in [self.editMenu, self.deleteMenu]:
                i.clear()
                i.addItems(options)

    def pickAction(self):
        # edit existing excercise
        if(self.editExisting.isChecked()):
            self.editExercise()

        # add new excercise
        elif(self.addNew.isChecked()):
            self.addExercise()

        # delete excercise
        else:
            self.deleteExercise()

        # refresh selection
        self.getExercises()  

    def editExercise(self):
        filename = self.editMenu.currentText()
        subprocess.call(
            ["notepad.exe", "resources/exercises/" + filename + ".txt"])

    def addExercise(self):
        filename = self.newExercise.text().replace(" ", "_")
        if(len(filename) == 0):
            filename = "newExercise"
        subprocess.call(
            ["notepad.exe", "resources/exercises/" + filename + ".txt"])

    def deleteExercise(self):
        filename = self.deleteMenu.currentText()
        os.remove("resources/exercises/" + filename + ".txt")
