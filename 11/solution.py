from collections import deque
from copy import deepcopy

with open('input.txt') as f:
    data = f.read()


groups = data.split('\n\n')

monkeys = []
counts = [0] * len(groups)
gcd = 1


for i, g in enumerate(groups):
    lines = g.splitlines()

    items = eval("[" + lines[1].split(': ')[1] + "]")
    items = deque(items)
    op = eval("lambda old:" + lines[2].split('=')[1])
    test = int(lines[3].split()[-1])
    t = int(lines[4].split()[-1])
    f = int(lines[5].split()[-1])

    gcd *= test
    monkeys.append((items, op, test, t, f))



def run(monkeys, counts, iterations, part_1):
    for _ in range(iterations):
        for i, m in enumerate(monkeys):
            items, op, test, t, f = m

            while items:
                item = items.popleft()
                item = op(item)

                if part_1 == True:
                    item //= 3
                else:
                    item %= gcd

                if item % test == 0:
                    monkeys[t][0].append(item)
                else:
                    monkeys[f][0].append(item)

                counts[i] += 1

    counts.sort(reverse=True)

    return counts[0] * counts[1]


monkeys2 = deepcopy(monkeys)
counts2 = deepcopy(counts)


print("Part 1:", run(monkeys, counts, 20, True))
print("Part 2:", run(monkeys2, counts2, 10000, False))
