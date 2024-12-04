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
similarity = []
for i in range(0, len(leftlist)):
    similarityScore = 0
    for j in range(0, len(rightlist)):
        if leftlist[i] == rightlist[j]:
            similarityScore += 1
    similarity.append(similarityScore)
print(similarity)
result = 0
for i in range(0, len(leftlist)):
    result += (similarity[i] * leftlist[i])
print(result)