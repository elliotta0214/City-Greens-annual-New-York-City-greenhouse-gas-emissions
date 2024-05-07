import json


f1 = open("data/stateemissions.csv", "r")
lines = f1.readlines()

dictionary ={}

for lineIndex in range(1, len(lines)):
    #split each line into another array of values separated by commas, use each value as needed
    splitLine = lines[lineIndex].split(",")

    if (splitLine[0] not in dictionary): 
        dictionary[splitLine[0]] = {}
    
    dictionary[splitLine[0]]["emissions"] = float(splitLine[1])


f1.close()

f2 = open("stateemissions.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()