import math

with open('input.txt') as f:
    data = f.read()


def get_direction(d):
    return {
        "R": ( 0, 1),
        "L": ( 0,-1),
        "U": ( 1, 0),
        "D": (-1, 0),
    }.get(d)


def distance(hpos, tpos):
    hx, hy = hpos
    tx, ty = tpos
    return math.sqrt((hx-tx)**2 + (hy-ty)**2)


def follow(hpos, tpos):
    hx, hy = hpos
    tx, ty = tpos
    dx, dy = hx - tx, hy - ty

    dx = -1 if dx == -2 else dx
    dx = 1 if dx == 2 else dx
    dy = -1 if dy == -2 else dy
    dy = 1 if dy == 2 else dy

    dist = distance(hpos, tpos)

    if dist <= math.sqrt(2):
        tx2, ty2 = tx, ty
    else:
        tx2, ty2 = tx + dx, ty + dy

    tpos2 = tx2, ty2

    return tpos2


def run(knots):
    visited = set()

    for line in data.splitlines():
        l, r  = line.split()
        dx, dy = get_direction(l)

        for _ in range(int(r)):
            visited.add((knots[-1]))
            knots[0] = knots[0][0] + dx, knots[0][1] + dy

            for i in range(len(knots) - 1):
                hpos, tpos = knots[i], knots[i+1]
                tpos = follow(hpos, tpos)
                knots[i+1] = tpos

        visited.add(knots[-1])
    
    return len(visited)


knots1 = [(0,0), (0,0)]
knots2 = [(0,0) for _ in range(10)]


print("Part 1:", run(knots1))
print("Part 2:", run(knots2))
