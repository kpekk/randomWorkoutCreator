from random import sample
import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def treeningplaan(*muscleGroups):

    #Dict for mapping indexes of x group's excercises in 2d array of excercises to muscle groups
    excercises = {'Legs':0, 'Biceps':0, 'Triceps':0, 'Core':0, 'Back':0, 'Shoulders':0, 'Chest':0}

    #Might add more muscle groups at one point, this lists them all
    files = os.listdir("resources/excercises/")

    ex = ["a"]*len(files)
    #For every file: open file, split the lines & save them to the 2d array 'ex'
    for index, file in enumerate(files):
        with open("resources/excercises/"+file, 'r') as f:
            ex[index] = f.read().splitlines()
            excercises[file.replace(".txt","")] = index
    
    #For every muscle group: pick a random sample of n to use in the workout plan
    workoutPlan = ""
    for group in muscleGroups:
        workoutPlan += group + ":-------\n"

        #3 random excercises, modify 2nd parameter to change the amount
        for excercise in sample(ex[excercises.get(group)],3):
            workoutPlan += excercise + "\n" 
                
    return workoutPlan
