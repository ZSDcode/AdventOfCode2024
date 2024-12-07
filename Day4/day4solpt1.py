
grid = []
def checkSurrounding(pos, rel_pos):
    global grid
    string = ''
    count = 0
    if rel_pos not in ["ne", "e", "se"]:
        for k in range(0, 4):
            string += grid[pos[0]][pos[1]+k]
        if string == 'XMAS':
            count += 1
            string = ''
        else:
            string = ''
    if rel_pos not in ["nw", "w", "sw"]:
        for k in range(0, 4):
            string += grid[pos[0]][pos[1]-k]
        if string == 'XMAS':
            count += 1
            string = ''
        else:
            string = ''
    if rel_pos not in ["nw", "n", "ne"]:
        for k in range(0, 4):
            string += grid[pos[0]-k][pos[1]]
        if string == 'XMAS':
            count += 1
            string = ''
        else:
            string = ''
    if rel_pos not in ["sw", "s", "se"]:
        for k in range(0, 4):
            string += grid[pos[0]+k][pos[1]]
        if string == 'XMAS':
            count += 1
            string = ''
        else:
            string = ''
    if rel_pos not in ["sw", "w", "nw", "n", "ne"]:
        for k in range(0, 4):
            string += grid[pos[0]-k][pos[1]-k]
        if string == 'XMAS':
            count += 1
            string = ''
        else:
            string = ''
    if rel_pos not in ["nw", "n", "ne", "e", "se"]:
        for k in range(0, 4):
            string += grid[pos[0]-k][pos[1]+k]
        if string == 'XMAS':
            count += 1
            string = ''
        else:
            string = ''
    if rel_pos not in ["nw", "w", "sw", "s", "se"]:
        for k in range(0, 4):
            string += grid[pos[0]+k][pos[1]-k]
        if string == 'XMAS':
            count += 1
            string = ''
        else:
            string = ''
    if rel_pos not in ["sw", "s", "se", "e", "ne"]:
        for k in range(0, 4):
            string += grid[pos[0]+k][pos[1]+k]
        if string == 'XMAS':
            count += 1
            string = ''
        else:
            string = ''
    return count


with open("C:\\Users\\Dylan\\gitrep\\AdventOfCode2024\\Day4\\Input Text.txt", "r") as file:
    for line in file:
        row = []
        for char in line:
            if char != '\n':
                row.append(char)
        grid.append(row)
landmarkLoc = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'X':
            landmarkLoc.append((i, j))
print(landmarkLoc)
topEdge = []
bottomEdge = []
westEdge = []
eastEdge = []
neCorner = []
nwCorner = []
seCorner = []
swCorner = []
central = []
for i in range(len(landmarkLoc)):
    if landmarkLoc[i][0] < 3 or landmarkLoc[i][0] > len(grid) - 4:
        if landmarkLoc[i][0] < 3:
            if landmarkLoc[i][1] < 3:
                nwCorner.append(landmarkLoc[i])
            elif landmarkLoc[i][1] > len(grid[i]) - 4:
                neCorner.append(landmarkLoc[i])
            else:
                topEdge.append(landmarkLoc[i])
        elif landmarkLoc[i][0] > len(grid) - 4:
            if landmarkLoc[i][1] < 3:
                swCorner.append(landmarkLoc[i])
            elif landmarkLoc[i][1] > len(grid) - 4:
                seCorner.append(landmarkLoc[i])
            else:
                bottomEdge.append(landmarkLoc[i])
    elif landmarkLoc[i][1] < 3 or landmarkLoc[i][1] > len(grid) - 4:
        if landmarkLoc[i][1] < 3:
            westEdge.append(landmarkLoc[i])
        else:
            eastEdge.append(landmarkLoc[i])
    else:
        central.append(landmarkLoc[i])
count = 0
directions = {"n": topEdge, "ne": neCorner, "e": eastEdge, "se": seCorner, "s": bottomEdge, 
              "sw": swCorner, "w": westEdge, "nw": nwCorner, "cen": central}

for key in directions.keys():
    print(f'{key}: {directions[key]}')
    for pos in directions[key]:
        if checkSurrounding(pos, key) != 0:
            count += checkSurrounding(pos, key)
print(count)
