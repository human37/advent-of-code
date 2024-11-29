# all test numbers multiplied together
# when we perform a check, we first mod the number by this number
# this is to prevent the numbers from getting too large, and the check will still work
# (I got this from a hint from reddit :D)
superMod = 9699690 

class Monkey:
    def __init__(self, monkey, starting_items, operation, test, if_test_pass, if_test_fail):
        self.monkey = monkey
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.if_test_pass = if_test_pass 
        self.if_test_fail = if_test_fail
    def __str__(self):
        return f'monkey: {self.monkey}\n starting_items: {self.starting_items}\n operation: {self.operation}\n test: {self.test} \n if_test_pass: {self.if_test_pass} \n if_test_fail: {self.if_test_fail}\n'

def perform_operation(item, operation):
    operation = operation.split()
    if operation[-2] == '+':
        if operation[-1] == 'old':
            return item + item
        return item + int(operation[-1])
    elif operation[-2] == '*':
        if operation[-1] == 'old':
            return item * item
        return item * int(operation[-1])

def perform_test(item, test):
    return item % test == 0

def monkey_bored(item):
    return item // 3

def take_turn(monkey):
    global monkeys
    global busiest_monkeys
    items = monkey.starting_items.copy()
    for item in items:
        if not monkey.monkey in busiest_monkeys:
            busiest_monkeys[monkey.monkey] = 1 
        else:
            busiest_monkeys[monkey.monkey] += 1
        old = item
        item = item % superMod
        item = perform_operation(item, monkey.operation)
        if perform_test(item, monkey.test):
            monkeys[monkey.if_test_pass].starting_items.append(item)
            monkey.starting_items.remove(old)
        else:
            monkeys[monkey.if_test_fail].starting_items.append(item)
            monkey.starting_items.remove(old)

monkeys = {} 
busiest_monkeys = {}
with open('p11-input.txt') as f:
    lines = f.readlines()
    name = None
    starting_items = None
    operation = None
    test = None
    if_test_pass = None
    if_test_fail = None
    for line in lines:
        if line.startswith('Monkey'):
            name = int(line.split()[1].replace(':', ''))
        elif line.strip().startswith('Starting'):
            starting_items = line.strip().replace('Starting items: ', '').split(',')
            starting_items = [int(item) for item in starting_items]
        elif line.strip().startswith('Operation'):
            operation = line.strip().replace('Operation: ', '')
        elif line.strip().startswith('Test'):
            test = int(line.strip().replace('Test: ', '').replace('divisible by ', ''))
            if_test_pass = int(lines[lines.index(line) + 1].strip().split()[-1])
            if_test_fail = int(lines[lines.index(line) + 2].strip().split()[-1])
        elif line == '\n':
            monkeys[name] = Monkey(name, starting_items, operation, test, if_test_pass, if_test_fail)
            name = None
            starting_items = None
            operation = None
            test = None
            if_test_pass = None
            if_test_fail = None

for i in range(10000):
    print("round", i)
    for k, v in monkeys.items():
        take_turn(monkeys[k])

print(busiest_monkeys)
m1 = max(busiest_monkeys, key=busiest_monkeys.get)
a = busiest_monkeys[m1]
busiest_monkeys.pop(m1)
m2 = max(busiest_monkeys, key=busiest_monkeys.get)
print(a * busiest_monkeys[m2])