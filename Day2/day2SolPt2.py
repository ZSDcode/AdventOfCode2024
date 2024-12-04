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

def QC(report):
    decreasing = False
    increasing = False
    gapTooBig = False
    duplicates = False
    for i in range(len(report)-1):
        if report[i] == report[i+1]:
            return ("dupe", i)
        elif report[i] > report[i+1]:
            if report[i] - report[i+1] > 3:
                return ("gap too big", i)
            elif decreasing == True:
                return ("switched", i)
            increasing = True
        elif report[i] < report[i+1]:
            if report[i+1] - report[i] > 3:
                return ("gap too big", i)
            if increasing == True:
                return ("switched", i)
            decreasing = True

quality = []
for report in reports:
    quality.append(QC(report))
for i in range(len(reports)):
    if (quality[i] != None):
        if (quality[i][0] == 'dupe'):
            reports[i].pop(quality[i][1])
            if (QC(reports[i]) == None):
                quality[i] = None
        elif (quality[i][0] == 'switched' or quality[i][0] == 'gap too big'):
            if (QC(reports[i][1:len(reports[i])]) == None):
                    print(reports[i][1:len(reports[i])])
                    quality[i] = None
            if (QC(reports[i][0:len(reports[i])-1]) == None):
                    print(reports[i][0:len(reports[i])-1])
                    quality[i] = None
            for j in range(1, len(reports[i])-1):
                checkerList = reports[i][0:j] + reports[i][j+1:len(reports[i])]
                if (QC(checkerList) == None):
                    print(checkerList)
                    quality[i] = None

sum = 0
for i in range(0, len(quality)):
    if (quality[i] == None):
        sum += 1
print(sum)