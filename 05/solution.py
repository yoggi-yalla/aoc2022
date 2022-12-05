with open('input.txt') as f:
    data = f.read()


def run(stacks, lines, part2):
    for line in lines:
        split = line.split()
        amt, f, t = int(split[1]), int(split[3]) - 1, int(split[5]) - 1

        temp = []
        for _ in range(amt):
            temp.append(stacks[f].pop())

        if part2:
            temp.reverse()

        for e in temp:
            stacks[t].append(e)
    
    out = []
    for s in stacks:
        out.append(s.pop())
    
    return "".join(out)



g1, g2 = data.split('\n\n')
lines1 = g1.splitlines()
lines2 = g2.splitlines()


stacks = [[] for _ in range(9)]

for pos in range(len(lines1[0])):
    if lines1[-1][pos].isnumeric():
        n = int(lines1[-1][pos]) - 1
        for line in lines1[:-1]:
            if line[pos] != ' ':
                stacks[n].append(line[pos])

for s in stacks:
    s.reverse()

stacks_copy = [[e for e in line] for line in stacks]


print("Part 1:", run(stacks, lines2, False))
print("Part 2:", run(stacks_copy, lines2, True))
