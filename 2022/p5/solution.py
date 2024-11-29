# [B]                     [N]     [H]
# [V]         [P] [T]     [V]     [P]
# [W]     [C] [T] [S]     [H]     [N]
# [T]     [J] [Z] [M] [N] [F]     [L]
# [Q]     [W] [N] [J] [T] [Q] [R] [B]
# [N] [B] [Q] [R] [V] [F] [D] [F] [M]
# [H] [W] [S] [J] [P] [W] [L] [P] [S]
# [D] [D] [T] [F] [G] [B] [B] [H] [Z]
#  1   2   3   4   5   6   7   8   9 

stack1 = ["D", "H", "N", "Q", "T", "W", "V", "B"]
stack2 = ["D", "W", "B"]
stack3 = ["T", "S", "Q", "W", "J", "C"]
stack4 = ["F", "J", "R", "N", "Z", "T", "P"]
stack5 = ["G", "P", "V", "J", "M", "S", "T"]
stack6 = ["B", "W", "F", "T", "N"]
stack7 = ["B", "L", "D", "Q", "F", "H", "V", "N"]
stack8 = ["H", "P", "F", "R"]
stack9 = ["Z", "S", "M", "B", "L", "N", "P", "H"]
stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

def move_crate(from_stack, to_stack, amount):
    crates = []
    for i in range(amount):
        item = stacks[from_stack - 1].pop()
        print("Moving crate %s from stack %s to stack %s" % (item, from_stack, to_stack))
        crates.append(item)
    crates.reverse()
    stacks[to_stack - 1].extend(crates)

with open("p5-input.txt") as f:
    for line in f:
        line = line.strip()
        line = line.split("from")
        amount = line[0].replace("move ", "")
        amount = int(amount)
        line = line[1].split("to")
        from_stack = int(line[0].strip())
        to_stack = int(line[1].strip())
        print("Moving {} from {} to {}".format(amount, from_stack, to_stack))
        move_crate(from_stack, to_stack, amount)

for i in range(len(stacks)):
    print("Stack {}: {}".format(i + 1, stacks[i].pop()))
