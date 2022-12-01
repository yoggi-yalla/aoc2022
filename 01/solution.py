with open('input.txt') as f:
    data = f.read()


sums = []
for group in data.split('\n\n'):
    s = 0
    for line in group.splitlines():
        s += int(line)
    sums.append(s)

sums.sort(reverse=True)

print("Part 1:", sums[0])
print("Part 2:", sum(sums[:3]))
