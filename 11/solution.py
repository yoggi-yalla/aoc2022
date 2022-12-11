from collections import defaultdict
from collections import deque
import math

with open('input.txt') as f:
    data = f.read()


def parse_data(data):
    monkeys = {}
    gcd = 1
    groups = data.split('\n\n')
    for i, g in enumerate(groups):
        lines = g.splitlines()
        items = eval("[" + lines[1].split(': ')[1] + "]")
        items = deque(items)
        op = lines[2].split(': ')[1].replace('old', 'item').replace('new', 'item')
        test = int(lines[3].split()[-1])
        t = int(lines[4].split()[-1])
        f = int(lines[5].split()[-1])
        gcd *= test

        monkeys[i] = (items, op, test, t, f)
    return monkeys, gcd


def monkey_business(business):
    return math.prod(sorted(business.values(), reverse=True)[:2])


for part in (1,2):
    monkeys, gcd = parse_data(data)
    business = defaultdict(int)
    for n in range(20 if part == 1 else 10000):
        for i in range(len(monkeys)):
            m = monkeys[i]
            items, op, test, t, f = m
            for _ in range(len(items)):
                item = items.popleft()
                exec(op)

                if part == 1:
                    item //= 3
                else:
                    item %= gcd

                if item % test == 0:
                    monkeys[t][0].append(item)
                else:
                    monkeys[f][0].append(item)

                business[i] += 1

    print(f"Part {part}:", monkey_business(business))
