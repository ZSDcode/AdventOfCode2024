row = ''
with open("C:\\Users\\Dylan\\gitrep\\AdventOfCode2024\\Day3\\Input File.txt", "r") as file:
    for line in file:
        row += line
valid = []
enabled = 1
for i in range(0, len(row)):
    if row[i] == 'd':
        if row[i:i+4] == 'do()':
            print(f"do at {i}")
            enabled = 1
        elif row[i:i+7] == "don't()":
            print(f"don't at {i}")
            enabled = 2
    checkString = ''
    if row[i] == 'm':
        if row[i:i+4] == 'mul(':
            indexOfClosed = 0
            for j in range(i, len(row)):
                if row[j] == ')':
                    indexOfClosed = j
                    break
            checkString = row[i:indexOfClosed+1]
            indexOfComma = 0
            for j in range(0, len(checkString)):
                if checkString[j] == ',':
                    indexOfComma = j
                    break
            if (checkString[4:indexOfComma].isnumeric()):
                if (checkString[indexOfComma+1:len(checkString)-1].isnumeric()):
                    if enabled == 1:
                        print(enabled)
                        valid.append(checkString)
results = 0
for validExp in valid:
    indexOfComma = 0
    for j in range(0, len(validExp)):
                if validExp[j] == ',':
                    indexOfComma = j
    result = int(validExp[4:indexOfComma]) * int(validExp[indexOfComma+1:len(checkString)-1])
    results += result
print(results)