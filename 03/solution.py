import string

with open('input.txt') as f:
    data = f.read()


p = 0
for line in data.splitlines():
    left, right = line[:len(line)//2], line[len(line)//2:]
    left, right = set(left), set(right)

    intersection = set.intersection(left, right)
    item = next(iter(intersection))

    p += string.ascii_letters.find(item) + 1
    
print("Part 1:", p)


lines = data.splitlines()

p = 0
i = 0
while i < len(lines):
    e1, e2, e3 = lines[i], lines[i+1], lines[i+2]
    e1, e2, e3 = set(e1), set(e2), set(e3)

    intersection = set.intersection(e1, e2, e3)
    badge = next(iter(intersection))

    p += string.ascii_letters.find(badge) + 1
    i += 3

print("Part 2:", p)
