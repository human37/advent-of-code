from anytree import Node, RenderTree
import io

f = io.open('p7-input.txt', 'r')
line = f.readline()
line = line.split()
root = Node("/")
current = root
while line != '':
    if len(line) == 0:
        break
    if line[0] == "$":
        command = line
        if command[1] == "cd":
            if command[2] == "/":
                current = root 
            elif command[2] == "..":
                current = current.parent 
            else:
                found = False
                for child in current.children:
                    if child.name == command[2]:
                        current = child
                        found = True
                if not found:
                    print("No such directory")
        elif command[1] == "ls":
            line = f.readline()
            line = line.split()
            done = False
            while not done and line[0] != "$" :
                if line[0] == "dir":
                    newDir = Node(line[1], parent=current)
                else:
                    try:
                        size = int(line[0])
                        newFile = Node(line[0], parent=current)
                    except:
                        print("Not a number", line)
                        continue
                line = f.readline()
                line = line.split()
                if len(line) == 0:
                    done = True 
            continue
    line = f.readline()
    line = line.split()
        
for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))
f.close()

l = {} 
def sumDirs(node):
    sum = 0
    for child in node.children:
        if child.is_leaf:
            sum += int(child.name)
        else:
            sum += sumDirs(child)
    l[node] = sum
    return sum
sumDirs(root)
print(l)

maxSpace = 70000000
neededSpace = 30000000
a = 0 
for key in l:
    if l[key] > a: 
        a = l[key]

availableSpace = maxSpace - a
spaceToFree = neededSpace - availableSpace

b = {}
for key in l:
    diff = l[key] - spaceToFree
    if diff >= 0:
        b[diff] = l[key]

asd = 999999999999
for key in b:
    if key < asd:
        asd = key
print(b[asd], spaceToFree)
