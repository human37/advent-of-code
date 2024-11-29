current_cycle = 1
x = 1
noop_cycles = 1
add_cycles = 2
instructions = []
cyclesMap = {}
crtScreen = ["."] * 239

with open('p10-input.txt') as f:
    instructions = f.readlines()

def parse_instruction(instruction):
    if instruction.startswith('noop'):
        return 'noop' 
    return int(instruction.split()[1])

def add_cycles_to_current_cycle(amount):
    global current_cycle
    global add_cycles
    for _ in range(amount):
        cyclesMap[current_cycle] = x 
        draw_crt_pixels(current_cycle, cyclesMap[current_cycle])
        current_cycle += 1

def draw_crt_pixels(current_cycle, x):
    global crtScreen
    if abs(x - current_cycle) <= 3:
        crtScreen[current_cycle] = '#'

def draw_screen():
    current_divisor = 0 
    for cycle, sprite in cyclesMap.items():
        if abs((cycle - current_divisor - 1) - sprite) < 2:
            print('#', end='')
        else:
            print('.', end='')
        if cycle % 40 == 0 and cycle != 0:
            current_divisor += 40
            print("   ", cycle)

for instruction in instructions:
    instruction = parse_instruction(instruction)
    if instruction == 'noop':
        add_cycles_to_current_cycle(1)
    else:
        add_cycles_to_current_cycle(add_cycles)
        x += instruction

draw_screen()
