from collections import defaultdict

with open('input.txt') as f:
    data = f.read()


tree = defaultdict(list)
lines = data.splitlines()
lines.reverse()

cwd = tuple()

while lines:
    line = lines.pop()
    if line == "$ cd ..":
        cwd = tuple((*cwd[:-1],))
        continue
    if line.startswith('$ cd'):
        cwd = tuple((*cwd, line.split()[-1]))
        continue

    if line == "$ ls":
        while lines:
            subline = lines.pop()
            if subline.startswith('$'):
                lines.append(subline)
                break
            
            l, r = subline.split()
            if l.isnumeric():
                tree[cwd].append([r, int(l)])
            else:
                tree[cwd].append(tuple((*cwd, r)))


def size(cwd, tree):
    s = 0

    node = tree[cwd]
    for subnode in node:
        if type(subnode) == list:
            s += subnode[-1]
        else:
            s += size(subnode, tree)

    return s


sizes = []
for cwd in tree:    
    sizes.append(size(cwd, tree))
sizes.sort()


part1 = 0
for c in sizes:
    if c >= 100000:
        break
    part1 += c
print("Part 1:", part1)


total_memory = 70000000
free_memory = total_memory - sizes[-1]
missing_memory = 30000000 - free_memory

for s in sizes:
    if s >= missing_memory:
        print("Part 2:", s)
        break
