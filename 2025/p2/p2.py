input_file = "input.txt"
answer = 0

def parse_input():
    input = []
    with open(input_file) as f:
        for line in f:
            if line != "":
                input = line.strip().split(",")
    return input

def solution_p2(input):
    global answer
    for id_range in input:
        start, end = id_range.split("-")
        process_range(int(start), int(end))
    print("solution p2:", answer)

def process_range(start, end):
    global answer
    for i in range(start, end+1):
        id = str(i)
        id_length = len(id)
        parts = []
        for j in range(1, id_length+1):
            parts.append(id[:j])
        invalid = False
        for part in parts:
            occurences = id.count(part)
            if occurences < 2:
                continue
            if occurences * len(part) == id_length:
                invalid = True
        if invalid:
            answer += i


def main():
    input = parse_input()
    solution_p2(input)



if __name__ == "__main__":
    main();

