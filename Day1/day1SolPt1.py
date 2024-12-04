row = []
with open("C:\\Users\\Dylan\\gitrep\\AdventOfCode2024\\Day1\\Input file.txt", "r") as file:
    for line in file:
        row.append(line.strip())
leftlist = []
rightlist = []
firstSpaceIdx = 0
lastSpaceIdx = 0
for i in range(0, len(row)):
    for j in range(0, len(row[i])):
        if row[i][j] == ' ':
            firstSpaceIdx = j
            break
    for j in range(len(row[i])-1, -1, -1):
        if row[i][j] == ' ':
            lastSpaceIdx = j
    leftlist.append(int(row[i][0:firstSpaceIdx]))
    rightlist.append(int(row[i][lastSpaceIdx+1:]))
leftlist.sort()
rightlist.sort()
distance = []
for i in range(0, len(leftlist)):
    if leftlist[i] > rightlist[i]:
        distance.append(leftlist[i] - rightlist[i])
    else:
        distance.append(rightlist[i]-leftlist[i])
totDist = 0
for i in range(0, len(distance)):
    totDist += distance[i]
print(totDist)