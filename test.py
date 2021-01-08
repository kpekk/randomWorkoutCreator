from random import sample
jalad = ["Squats","Lunges","Step-ups","Bulgarian split squats","Leg press","Romanian deadlift","Jalad surumine eest",
        "Jalad surumine tagant","Calf raise"]
biits = ["DB curls","Two-step spider curls","BB curls","Alternating DB hammer curls","Zottman curls",
        "BB bent over row","Chin ups","BB reverse curls"]
triits = ["Rope tricep pushdown","Skullcrushers","DB overhead extensions","DB close grip bench press","One arm lat pulldowns",
        "Kickbacks","Machine triceps extensions","Rope cable overhead extension"]
core = ["Ab Wheel Rollout","Three-Point Plank","Single Leg Romanian Deadlift","Weighted windshield wipers",
        "Reverse Crunches","Hanging Leg Raise","Dipi jaamas jalgade L-tõste","Superman Hold","Flutter Kick",
        "Russian twists","Cable wood choppers","Plank","Lamav jalgratas", "Lying leg raise"]
selg = ["Lat pulldown","Seated cable row","DB single arm row","BB bent over row","T bar row","Chest supported DB row",
        "Bent over DB row (alternating)","Kettlebell swings","Deadlift", "Pull ups"]
õlad = ["Arnold press","BB Overhead Shoulder Press","Seated DB Shoulder Press","Front Raise",
        "Bent-Over DB Lateral Raise","DB Lateral Raise","DB shoulder press","Reverse Pec Deck Fly",
        "Reverse Cable Crossover","One-Arm Cable Lateral Raise","Standing BB Shrugs"]
rind = ["Diamond pushups","Incline DB Bench Press","Rinnaltsurumine, poolistudes","Rinnaltsurumine kitsalt",
        "Dipid","Rinnaltsurumine","Plate Press-Out","Seated Pec Deck Machine","Cable Crossover"]

    #see dict on pärast koodi lihtsustamiseks
harjutused = {'jalad':jalad, 'biits':biits, 'triits':triits, 'core':core, 'selg':selg, 'õlad':õlad, 'rind':rind}

#for element in sample(jalad,3):
#    print(element)
data = harjutused.get("jalad","")
for elem in data:
    print(elem)
