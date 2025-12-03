input_file = "input.txt"
answer = 0

def parse_input():
    input = []
    with open(input_file) as f:
        for line in f:
            if line != "":
                input = line.strip().split(",")
    return input

def solution_p1(input):
    global answer
    for id_range in input:
        start, end = id_range.split("-")
        process_range(int(start), int(end))
    print("solution_p1:", answer)

def process_range(start, end):
    global answer
    for i in range(start, end+1):
        id = str(i)
        id_length = len(id)
        if id_length % 2 == 1:
            continue
        half_length = int(id_length / 2)
        if id[:half_length] == id[half_length:]:
            answer += int(id)
            print("invalid id:", id)





def main():
    input = parse_input()
    solution_p1(input)



if __name__ == "__main__":
    main();

