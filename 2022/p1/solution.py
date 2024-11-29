elves = []
elve = []
with open("p1-input.txt") as f:
    for line in f:
        if line == "\n":
            elves.append(elve)
            elve = []
            continue
        line = line.strip()
        elve.append(int(line))

a = []
for elve in elves:
    a.append(sum(elve))
    
one = max(a)

a.remove(max(a))

two = max(a)

a.remove(max(a))

three = max(a)

print(one + two  + three)