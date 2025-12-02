input_file = "input.txt"
position = 50
answer = 0

def parse_input():
    input = []
    with open(input_file) as f:
        for line in f:
            if line != "":
                input.append(line.strip())
    return input

def solution_p1(input):
    global position, answer

    for rotation in input:
        if rotation[0] == "R":
            rotate_right(int(rotation[1:]))
        elif rotation[0]== "L":
            rotate_left(int(rotation[1:]))
        if position == 0:
            answer += 1
    print("solution part 1:", answer)

def rotate_left(distance):
    global position
    for rotation in range(distance):
        if position == 0:
            position = 99
        else:
            position -= 1

def rotate_right(distance):
    global position
    for rotation in range(distance):
        if position == 99:
            position = 0
        else:
            position += 1


def main():
    input = parse_input()
    solution_p1(input)



if __name__ == "__main__":
    main();

