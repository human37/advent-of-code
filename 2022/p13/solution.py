import json
from functools import cmp_to_key


def compare(left, right):
    if type(left) == type(right):
        if isinstance(left, (int)) and isinstance(right, (int)):
            if left == right:
                return None
            if left < right:
                return -1
            return 1
        elif isinstance(left, (list)) and isinstance(right, (list)):
            for i in range(len(left)):
                if i >= len(right):
                    return 1
                res = compare(left[i], right[i])
                if res is None:
                    continue
                return res
            if len(left) == len(right):
                return None
            return -1

    if isinstance(left, (int)) and not isinstance(right, (int)):
        return compare([left], right)

    elif not isinstance(left, (int)) and isinstance(right, (int)):
        return compare(left, [right])

    print("OOPS")


letter_cmp_key = cmp_to_key(compare)


def main():
    pairs = []
    with open("p13-input.txt") as f:
        lines = f.readlines()
    div1 = [[2]]
    div2 = [[6]]
    pairs.append(div1)
    pairs.append(div2)
    for line in lines:
        if line == "\n":
            continue
        pair = json.loads(line)
        pairs.append(pair)

    pairs.sort(key=letter_cmp_key)
    for pair in pairs:
        print(pair)
    print("index of div1: ", pairs.index(div1) + 1)
    print("index of div2: ", pairs.index(div2) + 1)
    print("product: ", (pairs.index(div1) + 1) * (pairs.index(div2) + 1))


main()
