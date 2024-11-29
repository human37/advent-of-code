# read in text file and print out the longest line
with open('p8-input.txt') as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        grid.append([*line.strip()])

gridSize = len(grid)
for row in grid:
    print(row)

# determine if tree is visible
def is_visible(grid, x, y):
    # check if on edge
    height = grid[x][y]
    print(f'height: {height}, x: {x}, y: {y}')
    if x == 0 or y == 0 or x == gridSize - 1 or y == gridSize - 1:
        return 0
    # check up 
    upScore = 1
    for i in range(y, 0, -1):
        if i == y:
            continue
        if grid[x][i] >= height:
            break
        upScore += 1
    # check down
    downScore = 0
    for i in range(y, gridSize):
        if i == y:
            continue
        if grid[x][i] >= height:
            break
        downScore += 1
    # check left
    leftScore = 1
    for i in range(x, 0, -1):
        if x == i:
            continue
        if grid[i][y] >= height:
            break
        leftScore += 1
    # check right
    rightScore = 1
    for i in range(x, gridSize):
        if x == i:
            continue
        if grid[i][y] >= height:
            break
        rightScore += 1


    total =  upScore * downScore * leftScore * rightScore 
    print(f'height: {height}, up: {upScore}, left: {leftScore}, down: {downScore}, right: {rightScore}')
    return total

# count number of visible trees
maxScore = 0
for x in range(gridSize):
    for y in range(gridSize):
        score =  is_visible(grid, x, y)
        if score > maxScore:
            maxScore = score

# print(is_visible(grid, 3, 2))
print(maxScore)