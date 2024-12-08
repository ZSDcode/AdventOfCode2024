import math

rules = []
inputs = []
with open("C:\\Users\\Dylan\\gitrep\\AdventOfCode2024\\Day5\\Input Text.txt", 'r') as file:
    for line in file:
        if '|' in line:
            dict = {}
            string = line.strip('\n')
            separatorIdx=string.index('|')
            dict[int(string[0:separatorIdx])] = int(string[separatorIdx+1:len(string)])
            rules.append(dict)
            dict = {}
        if ',' in line:
            string = line.strip('\n')
            input = []
            placeholderIdx = 0
            for i in range(len(string)):
                if string[i] == ',':
                    input.append(int(string[placeholderIdx:i]))
                    placeholderIdx = i+1
            input.append(int(string[placeholderIdx:len(string)]))
            inputs.append(input)

def check(update):
    follow = True
    for i in range(len(update)-1):
        consideredRules = []
        for j in range(len(rules)):
            if update[i] in rules[j].keys():
                consideredRules.append(rules[j][update[i]])
        for j in range(i+1, len(update)):
            if update[j] not in consideredRules:
                follow = False
    return follow

def swap(invalid, indexBefore, indexAfter):
    placeholder = invalid[indexBefore]
    invalid[indexBefore] = invalid[indexAfter]
    invalid[indexAfter] = placeholder
    return invalid

def correct(invalid):
    if check(invalid):
        return invalid
    else:
        for i in range(len(invalid)-1):
            consideredRules = []
            for j in range(len(rules)):
                if invalid[i] in rules[j].keys():
                    consideredRules.append(rules[j][invalid[i]])
            for j in range(i+1, len(invalid)):
                if invalid[j] not in consideredRules:
                    corrected = swap(invalid, i, j)
                    return correct(corrected)

sum = 0
for input in inputs:
    if not check(input):
        correctedInput = correct(input)
        sum += correctedInput[math.floor(len(correctedInput)/2)]
print(sum)
