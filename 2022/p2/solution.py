def play(opponent, you):
    if opponent == 'A' and you == 'X':
        return "Z" 
    elif opponent == 'A' and you == 'Y':
        return "X"
    elif opponent == 'A' and you == 'Z':
        return "Y"
    elif opponent == 'B' and you == 'X':
        return "X"
    elif opponent == 'B' and you == 'Y':
        return "Y" 
    elif opponent == 'B' and you == 'Z':
        return "Z" 
    elif opponent == 'C' and you == 'X':
        return "Y" 
    elif opponent == 'C' and you == 'Y':
        return "Z" 
    elif opponent == 'C' and you == 'Z':
        return "X" 
    else:
        return False

def shape(you):
    if you == 'X':
        return 1
    elif you == 'Y':
        return 2
    elif you == 'Z': 
        return 3

def score(you):
    if you == 'X':
        return 0
    elif you == 'Y':
        return 3
    elif you == 'Z': 
        return 6

total = []
with open("p2-input.txt") as f:
    for line in f:
        a = line.split()
        opponent = a[0]
        you = a[1]
        total.append(shape(play(opponent, you)) + score(you))

print(sum(total))