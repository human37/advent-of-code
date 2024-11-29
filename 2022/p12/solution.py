from collections import deque

def find_elev_diff(a, b):
    if a == "S":
        a = "a"
    elif a == "E":
        a = "z"
    if b == "S":
        b = "a"
    elif b == "E":
        b = "z"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.index(b) - alphabet.index(a)

def make_key(i, j):
    return "x" + str(i) + "y" + str(j)

def build_graph(lines):
    graph = {}
    starts = [] 
    end = None
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S" or lines[i][j] == "a":
                starts.append(make_key(i, j))
            if lines[i][j] == "E":
                end = make_key(i, j)
            graph[make_key(i, j)] = []
            # check up
            if i > 0:
                if find_elev_diff(lines[i][j], lines[i-1][j]) <= 1:
                    if make_key(i-1, j) in graph[make_key(i, j)]:
                        continue
                    graph[make_key(i, j)].append(make_key(i-1, j))
            # check down
            if i < len(lines) - 1:
                if find_elev_diff(lines[i][j], lines[i+1][j]) <= 1:
                    if make_key(i+1, j) in graph[make_key(i, j)]:
                        continue
                    graph[make_key(i, j)].append(make_key(i+1, j))
            # check left
            if j > 0:
                if find_elev_diff(lines[i][j], lines[i][j-1]) <= 1:
                    if make_key(i, j-1) in graph[make_key(i, j)]:
                        continue
                    graph[make_key(i, j)].append(make_key(i, j-1))
            # check right
            if j < len(lines[i]) - 1:
                if find_elev_diff(lines[i][j], lines[i][j+1]) <= 1:
                    if make_key(i, j+1) in graph[make_key(i, j)]:
                        continue
                    graph[make_key(i, j)].append(make_key(i, j+1))
    return graph, starts, end


def check_distance(graph, start, end):
    queue = deque([(start, 0)])
    seen = set()
    while queue:
        node, distance = queue.popleft()
        if node in seen:
            continue
        seen.add(node)
        if node == end:
            return distance
        for adjacent in graph.get(node):
            queue.append((adjacent, distance + 1))

def main():
    with open('p12-input.txt') as f:
        lines = f.readlines()
        lines = [line.replace("\n", "") for line in lines]
        lines = [list(line) for line in lines]
    graph, starts, end = build_graph(lines)
    dists = []
    for start in starts:
        dist = check_distance(graph, start, end)
        if dist is not None:
            dists.append(dist)
    print("dists", min(dists))

main()
