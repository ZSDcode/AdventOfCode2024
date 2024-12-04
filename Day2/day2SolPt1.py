row = []
with open("C:\\Users\\Dylan\\gitrep\\AdventOfCode2024\\Day2\\Input File.txt", "r") as file:
    for line in file:
        row.append(line.strip())
reports = []
for i in range(0, len(row)):
    placeholder = 0
    report = []
    for j in range(0, len(row[i])):
        if row[i][j] == ' ':
            level = int(row[i][placeholder:j])
            placeholder = j+1
            report.append(level)
    report.append(int(row[i][placeholder:]))
    reports.append(report)
qualityCheck = [False] * len(reports)
for i in range(0, len(reports)):
    sameLevel = False
    decreasing = False
    increasing = False
    gapTooBig = False
    for j in range(0, len(reports[i])-1):
        if reports[i][j] == reports[i][j+1]:
            sameLevel = True
        if reports[i][j] > reports[i][j+1]:
            if (reports[i][j] - reports[i][j+1]) > 3:
                gapTooBig = True
            decreasing = True
        if reports[i][j] < reports[i][j+1]:
            if (reports[i][j+1] - reports[i][j]) > 3:
                gapTooBig = True
            increasing = True
    if sameLevel == False:
        if decreasing != increasing:
            if gapTooBig == False:
                qualityCheck[i] = True
sum = 0
for i in range(0, len(qualityCheck)):
    if (qualityCheck[i] == True):
        sum += 1
print(sum)