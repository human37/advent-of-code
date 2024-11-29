my_list = []
def find_priority(a):
    lower = "abcdefghijklmnopqrstuvwxyz"
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if a in lower:
        return lower.index(a) + 1
    if a in caps:
        return caps.index(a) + 27 
    return -1

def split(list_a, chunk_size):
  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

all_elve_groups = []
with open("p3-input.txt") as f:
    is_three = 0
    for line in f:
       my_list.append(line.strip())

all_elve_groups = split(my_list, 3)

totals = []
for elve_group in all_elve_groups:
    common_item = False
    for item in elve_group[0]:
        if item in elve_group[1] and item in elve_group[2]:
            common_item = item
            break
    if common_item:
        totals.append(find_priority(common_item))


print(sum(totals))
print(len(totals))
