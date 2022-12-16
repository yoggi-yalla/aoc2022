import itertools
import re

with open('input.txt') as f:
    data = f.read()


def x_dst(p1, p2):
    return abs(p1[0] - p2[0])


def y_dst(p1, p2):
    return abs(p1[1] - p2[1])


def dst(p1,p2):
    return x_dst(p1, p2) + y_dst(p1, p2)


def get_lines(sensor):
    x, y, d = sensor
    return (
        ((x-d, y), (x, y+d)),
        ((x-d, y), (x, y-d)),
        ((x, y-d), (x+d, y)),
        ((x, y+d), (x+d, y)),
    )


def intersection_point(l1, l2):
    (x1, y1), (x2, y2) = l1
    (x3, y3), (x4, y4) = l2

    k1 = (y2-y1) // (x2-x1)
    k2 = (y4-y3) // (x4-x3)

    m1 = y1 - k1 * x1
    m2 = y3 - k2 * x3

    if k1 == k2:
        return set()
    else:
        x = abs((m2 - m1) // (2 * k1))
        if x < 0 or x > 4000000:
            return set()
        elif (x1 <= x <= x2) and (x3 <= x <= x4):
            return set([(x, k1 * x + m1)])
        else:
            return set()


def contains(p, sensor):
    x, y, d = sensor
    xx, yy = p
    dd = d - abs(y-yy)
    if dd >= 0:
        if x-dd <= xx <= x+dd:
            return True
    return False


# Parse data
pattern = re.compile(r".*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)")

sensors = set()
beacons = set()
for line in data.splitlines():
    x, y, xx, yy = map(int, re.match(pattern, line).groups())

    d = dst((x,y),(xx,yy))

    sensors.add((x,y,d))
    beacons.add((xx,yy))


# Part 1
row = 2000000
x_ranges = []
for x, y, d in sensors:
    dd = d - abs(y - row)
    if dd >= 0:
        x_ranges.append((x - dd, x + dd))
x_ranges.sort()


merged_x_ranges = []
x1, x2 = x_ranges[0]
for xx1, xx2 in x_ranges[1:]:
    if xx1 > x2:
        merged_x_ranges.append((x1,x2))
        x1, x2 = xx1, xx2
    elif xx2 > x2:
        x2 = xx2
    else:
        continue
merged_x_ranges.append((x1, x2))


count = 0
for x1, x2 in merged_x_ranges:
    count += (x2 - x1)

print("Part 1:", count)


# Part 2
lines = set()
for s in sensors:
    for l in get_lines(s):
        lines.add(l)


intersections = set()
for l1, l2 in itertools.combinations(lines, 2):
    intersections |= intersection_point(l1, l2)


x_candidates = set()
y_candidates = set()
for p1, p2 in itertools.combinations(intersections, 2):
    if x_dst(p1, p2) == 2 and y_dst(p1, p2) == 0:
        x_candidates.add((p1,p2))
    if x_dst(p1, p2) == 0 and y_dst(p1, p2) == 2:
        y_candidates.add((p1, p2))


xy_candidates = set()
for p1, _ in x_candidates:
    for p2, _ in y_candidates:
        if x_dst(p1, p2) == 1 and y_dst(p1, p2) == 1:
            xy_candidates.add((p2[0], p1[1]))


for p in xy_candidates:
    for s in sensors:
        if contains(p, s):
            break
    else:
        print("Part 2:", 4000000 * p[0] + p[1])


import time
print(time.process_time()) # 0.07s
