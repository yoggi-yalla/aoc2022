with open('input.txt') as f:
    data = f.read()

p1 = 0
p2 = 0
for line in data.splitlines():
    left, right = line.split(',')
    low1, high1, low2, high2 = map(int, (*left.split('-'), *right.split('-')))

    range1, range2 = set(list(range(low1, high1 + 1))), set(list(range(low2, high2 + 1)))

    if range1.issuperset(range2) or range2.issuperset(range1):
        p1 += 1
    
    if range1.intersection(range2):
        p2 += 1

print("Part 1:", p1)
print("Part 2:", p2)
