import json


f1 = open("data/gasemissions.csv", "r")
lines = f1.readlines()

dictionary ={}

for lineIndex in range(1, len(lines)):
    #split each line into another array of values separated by commas, use each value as needed
    splitLine = lines[lineIndex].split(",")

    if (splitLine[0] not in dictionary): 
        dictionary[splitLine[0]] = {}
    
    dictionary[splitLine[0]]["MMBTU/metric ton steam"] = float(splitLine[1])
    dictionary[splitLine[0]]["CO2 - kg per metric ton steam"] = float(splitLine[2]) 
    dictionary[splitLine[0]]["CH4 - kg per metric ton steam"] = float(splitLine[3])
    dictionary[splitLine[0]]["N2O - kg per metric ton steam"] = float(splitLine[4]) 
    dictionary[splitLine[0]]["CO2e - kg per metric ton steam"] = float(splitLine[5]) 

f1.close()

f2 = open("emissions.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()