rope = [(0, 0)] * 10
rope_positions = {}
rope_length = 2
movements = []
with open('p9-input.txt') as f:
    movements = f.readlines()

def calc_distance(head, tail):
    return max(abs(head[1] - tail[1]), abs(head[0] - tail[0]))

def is_tail_adjacent(head, tail):
    return calc_distance(head, tail) < rope_length 

def parse_movement(movement):
    return movement.split()[0], int(movement.split()[1])

def move_head(x, y):
    global rope_positions
    rope[0] = x, y
    for i in range(len(rope) - 1):
        new_tail = move_tail(rope[i], rope[i + 1])
        rope[i + 1] = new_tail
        if i + 1 == 9:
            rope_positions[new_tail] = True

def move_tail(head, tail):
    global rope_positions
    if not is_tail_adjacent(head, tail):
        if head[0] == tail[0] or head[1] == tail[1]:
            if head[0] > tail[0]:
                tail = tail[0] + 1, tail[1]
            elif head[0] < tail[0]:
                tail = tail[0] - 1, tail[1]
            elif head[1] > tail[1]:
                tail = tail[0], tail[1] + 1
            elif head[1] < tail[1]:
                tail = tail[0], tail[1] - 1
        else:
            if head[0] > tail[0] and head[1] > tail[1]:
                tail = tail[0] + 1, tail[1] + 1
            elif head[0] > tail[0] and head[1] < tail[1]:
                tail = tail[0] + 1, tail[1] - 1
            elif head[0] < tail[0] and head[1] > tail[1]:
                tail = tail[0] - 1, tail[1] + 1
            elif head[0] < tail[0] and head[1] < tail[1]:
                tail = tail[0] - 1, tail[1] - 1
    return tail
            
for movement in movements:
    direction, length = parse_movement(movement)
    for i in range(length):
        if direction == 'U':
            move_head(rope[0][0], rope[0][1] + 1)
        elif direction == 'D':
            move_head(rope[0][0], rope[0][1] - 1)
        elif direction == 'L':
            move_head(rope[0][0] + 1, rope[0][1])
        elif direction == 'R':
            move_head(rope[0][0] - 1, rope[0][1])

print(len(rope_positions))