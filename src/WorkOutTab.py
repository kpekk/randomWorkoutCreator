import os, re
from PyQt5.QtWidgets import *
from themes import *
from treeningkava_main import *

class WorkOutTab(QWidget):
    def __init__(self, parent): 
        super(QWidget, self).__init__(parent)

        #disabling generate button if 'send to email' is selected but no app email is specified
        def updateGenerateButtonState():
            if(self.chooseEmail.isChecked()):
                self.generateButton.setDisabled(False)
                sender_email = ""
                with open("config\email.txt", "r+") as f:
                    sender_email = f.read().split("\n")

                sender_email = sender_email[0].strip()

                if sender_email == "":
                    self.generateButton.setDisabled(True)
                    self.generateButton.setText("No application email found!")

        def validateEmail():
            text = self.emailAddress.text()
            if re.match(r"[^@]+@[^@]+\.[^@]+", text):
                self.generateButton.setDisabled(False)
                self.generateButton.setText("I'm ready, hit it!")
            else:
                self.generateButton.setDisabled(True)
                self.generateButton.setText("Enter valid email")
            updateGenerateButtonState()

        #choose between sending the email and saving the output to 'workout.txt'
        def chooseOutput():
            #output goes to text file, no need to validate email
            if(self.chooseTxt.isChecked()):
                #disable email adress field 
                self.emailAddress.setDisabled(True)

                #enable generateButton
                self.generateButton.setDisabled(False)
                self.generateButton.setText("I'm ready, hit it!")
            
            #output is sent to email adress, validate the email field
            else:
                self.emailAddress.setDisabled(False)
                validateEmail()

        #calls the driver method
        def generate():
            #the first excercise is always included
            exercises = [self.option1.currentText()]
    
            #add 2nd and 3rd excercise if not excluded
            if not self.excludeExercise_2.isChecked():
                exercises.append(self.option2.currentText())
            if not self.excludeExercise_3.isChecked():
                exercises.append(self.option3.currentText())

            #getting the sample size from the sample_size.txt file
            sampleSize = ""
            with open("config\sample_size.txt") as f:
                sampleSize = int(f.read().strip())
           
            mail = self.emailAddress.text()

            #workout plan is sent to the email address
            if(self.chooseEmail.isChecked()):
                treeningkava_main("email", exercises,sampleSize, mail)

            #workout plan is saved to .txt file
            else:
                treeningkava_main("outputToTextFile",exercises,sampleSize, mail)

        #excluding excercises
        def checkExclude():
            self.option2.setDisabled(False)
            self.option3.setDisabled(False)

            #disable excluded parts to avoid confusion
            if self.excludeExercise_2.isChecked():
                self.option2.setDisabled(True)

            if self.excludeExercise_3.isChecked():
                self.option3.setDisabled(True)

        #Layout (aka the main widget)
        lay = QGridLayout(self)
    
        #1st excercise
        lay.addWidget(QLabel("Exercise type #1"),0,0)
        self.option1 = QComboBox()
        lay.addWidget(self.option1,0,1,1,3)

        #2nd excercise
        lay.addWidget(QLabel("Exercise type #2"),1,0)
        self.option2 = QComboBox()
        lay.addWidget(self.option2,1,1,1,2)
        #option to exclude 2nd excercise
        self.excludeExercise_2 = QCheckBox("Exclude")
        self.excludeExercise_2.stateChanged.connect(checkExclude)
        lay.addWidget(self.excludeExercise_2,1,3)

        #3rd excercise
        lay.addWidget(QLabel("Exercise type #3"),2,0)
        self.option3 = QComboBox()
        lay.addWidget(self.option3,2,1,1,2)
        #option to exluce 3rd excercise
        self.excludeExercise_3 = QCheckBox("Exclude")
        self.excludeExercise_3.stateChanged.connect(checkExclude)
        lay.addWidget(self.excludeExercise_3,2,3)

        #send the workout to email
        self.chooseEmail = QRadioButton()
        self.chooseEmail.setChecked(True)#default option
        self.chooseEmail.toggled.connect(chooseOutput)
        self.chooseEmailLabel = QLabel("Send me the workout via email")
        lay.addWidget(self.chooseEmailLabel,3,0,1,1)
        lay.addWidget(self.chooseEmail,3,1,1,1)

        #save the plan to workout.txt (no email)
        self.chooseTxt = QRadioButton();
        self.chooseTxt.toggled.connect(chooseOutput)
        self.chooseTxtLabel = QLabel("Save the workout to 'workout.txt'")
        lay.addWidget(self.chooseTxtLabel,3,2,1,1)
        lay.addWidget(self.chooseTxt,3,3,1,1)

        #email address field
        self.emailAddress = QLineEdit(self)
        self.emailAddress.setPlaceholderText("Email address")
        self.emailAddress.textChanged.connect(validateEmail)
        lay.addWidget(self.emailAddress,4,0,1,4)

        #driver code button
        self.generateButton = QPushButton("Enter valid email")
        lay.addWidget(self.generateButton,5,1,1,2)
        self.generateButton.clicked.connect(generate)
        #inactive if mail address field is empty
        self.generateButton.setDisabled(True)

        #set/refresh combobox options (will be called on every tabchange event)
        self.getExercises()

    #get all user-defined file names
    def getExercises(self):
        files = os.listdir("resources/exercises/")
        options = []
        for file in files:
            options.append(file.replace(".txt",""))
        
        #update excercise selection
        for i in [self.option1,self.option2,self.option3]:
            i.clear()
            i.addItems(options)