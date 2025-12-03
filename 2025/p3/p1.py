input_file = "input.txt"
answer = 0

def parse_input():
    input = []
    with open(input_file) as f:
        for line in f:
            input.append(line.strip())
    return input

def solution_p1(input):
    global answer
    for bank in input:
        largest_joltage = 0
        for start in range(len(bank)):
            for end in range(len(bank[start:])-1):
                joltage = int(bank[start] + bank[start+end+1])
                if joltage > largest_joltage:
                    largest_joltage = joltage
        answer += largest_joltage
    print("solution_p1:", answer)


def main():
    input = parse_input()
    solution_p1(input)



if __name__ == "__main__":
    main();

