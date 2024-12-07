grid = []

def checkSurroundings(pos):
    smallGrid = []
    smallRow = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            smallRow.append(grid[pos[0]+i][pos[1]+j])
        smallGrid.append(smallRow)
        smallRow = []
    up = ''
    down = ''
    left = ''
    right = ''
    for i in range(0, 3):
        up += smallGrid[0][i]
        down += smallGrid[2][i]
        left += smallGrid[i][0]
        right += smallGrid[i][2]
    if (up[0] == 'M' and up[2] == 'M') or (down[0] == 'M' and down[2] == 'M'):
        if (up[0] == 'S' and up[2] == 'S') or (down[0] == 'S' and down[2] == 'S'):
            return True
    if (left[0] == 'M' and left[2] == 'M') or (right[0] == 'M' and right[2] == 'M'):
        if (left[0] == 'S' and left[2] == 'S') or (right[0] == 'S' and right[2] == 'S'):
            return True

with open("C:\\Users\\Dylan\\gitrep\\AdventOfCode2024\\Day4\\Input Text.txt", "r") as file:
    for line in file:
        row = []
        for char in line:
            if char != '\n':
                row.append(char)
        grid.append(row)
landmarkLoc = []
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):
        if grid[i][j] == 'A':
            landmarkLoc.append((i, j))
print(landmarkLoc)
count = 0
for pos in landmarkLoc:
    if checkSurroundings(pos):
        count += 1
print(count)