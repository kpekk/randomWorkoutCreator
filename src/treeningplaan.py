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

    
def treeningplaan(muscleGroups,sample_size):

    #list of the excercise files
    files = os.listdir("resources/exercises/")

    #can't be sets, since the user might choose multiples of the same group
    groups = []
    exercise_samples = []

    #For every muscle group: pick a random sample of size n to use in the workout plan
    for group in muscleGroups:
        groups.append(group)

        exercises = []
        for file in files:
            if group == file.replace(".txt",""):
                with open("resources/exercises/"+file, 'r') as f:
                    exercises = f.read().splitlines()
    
        #generating random samples of size 'sample_size'
        if(len(exercises) < sample_size):
            exercise_samples.append(exercises)
        else:
            exercise_samples.append(sample(exercises,sample_size))
   

    return groups,exercise_samples
