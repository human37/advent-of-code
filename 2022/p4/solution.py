def make_full(r):
    r = r.split("-")
    start = int(r[0])
    end = int(r[1])
    ret = []
    for i in range(start, end + 1):
       ret.append(str(i))
    return ret

pairs = []
with open("p4-input.txt") as f:
    for line in f:
        line = line.strip()
        line = line.split(",")
        a, b = line[0], line[1]
        a  = make_full(a)
        b = make_full(b)
        ranges = {}
        found = False
        for c in a:
            ranges[c] = True
        for c in b:
            if c in ranges:
                pairs.append(line)
                break

print(len(pairs))