import re

pattern = re.compile(r".*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)")


with open('input.txt') as f:
    data = f.read()



sensors = set()
beacons = set()
ranges = set()


for line in data.splitlines():
    x, y, xx, yy = map(int, re.match(pattern, line).groups())

    sensors.add((x,y))
    beacons.add((xx,yy))

    d = abs(x-xx) + abs(y-yy)
    ranges.add((x,y,d))

ranges = sorted(list(ranges))


for row in range(4000000):
    r_set = set([(0,4000000)])

    for (x,y,d) in ranges:

        new_set = r_set.copy()

        dd = d - abs(y-row)

        if y-d <= row <= y+d:

            dl, dr = ((x - dd), (x + dd))

            for rl, rr in r_set:

                if dl > rr:
                    continue

                if dr < rl:
                    continue

                if dl <= rl and dr >= rr:
                    new_set.remove((rl, rr))
                    continue

                if dl > rl and dr < rr:
                    new_set.remove((rl, rr))
                    new_set.add((rl, dl-1))
                    new_set.add((dr+1, rr))
                    continue

                if dr >= rl:
                    new_set.remove((rl, rr))
                    new_set.add((dr+1, rr))
                    continue

                if d <= rr:
                    new_set.remove((rl, rr))
                    new_set.add((rl, dl-1))
                    continue

        r_set = new_set


    if r_set:
        print(row, r_set)
        break
