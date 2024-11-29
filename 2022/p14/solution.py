def create_cave(max_depth, max_width):
    cave = {}
    l = 500 - max_width // 2
    r = 500 + max_width // 2
    for i in range(l, r):
        cave[i] = [None] * max_depth
    return cave


def show_cave():
    global cave
    print()
    for i in range(10):
        print(i, end=" ")
        for _, value in cave.items():
            if value[i] == None:
                print(".", end="")
            else:
                print(value[i], end="")
        print()
    print()


def create_wall(start, end):
    global cave
    x1, y1 = start
    x2, y2 = end
    if x1 == x2:
        if y1 > y2:
            for i in range(y2, y1 + 1):
                cave[x1][i] = "#"
        else:
            for i in range(y1, y2 + 1):
                cave[x1][i] = "#"
    else:
        if x1 > x2:
            for i in range(x2, x1 + 1):
                cave[i][y1] = "#"
        else:
            for i in range(x1, x2 + 1):
                cave[i][y1] = "#"


def pour_sand(current):
    global cave
    global max_depth
    global max_width
    x, y = current
    if y == max_depth - 1:  # reached bottom
        print("reached bottom")
        return (x, y)
    if cave[x][y + 1] == None:
        return pour_sand((x, y + 1))
    elif cave[x][y + 1] == "#" or cave[x][y + 1] == "o":
        # attempt left diagonal
        if cave[x - 1][y + 1] == None:
            return pour_sand((x - 1, y + 1))
        # attempt right diagonal
        elif cave[x + 1][y + 1] == None:
            return pour_sand((x + 1, y + 1))
        # we are at rest
        else:
            if x == 500 and y == 0:
                return False
            return (x, y)


def start():
    global cave
    count = 1
    while True:
        res = pour_sand((500, 0))
        if res == False:
            break
        x, y = res
        cave[x][y] = "o"
        count += 1
    print(count)
    show_cave()


def main():
    global cave
    with open("p14-example-input.txt") as f:
        whys = []
        for line in f:
            line = line.strip().split(" -> ")
            for i in range(len(line) - 1):
                coord1 = line[i].split(",")
                coord1 = (int(coord1[0]), int(coord1[1]))
                coord2 = line[i + 1].split(",")
                coord2 = (int(coord2[0]), int(coord2[1]))
                print(coord1, coord2)
                whys.append(coord1[1])
                whys.append(coord2[1])
                create_wall(coord1, coord2)
    return max(whys) + 2


max_depth = 200
max_width = 200
cave = create_cave(max_depth, max_width)
max_depth = main()
start()
