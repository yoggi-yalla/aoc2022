import itertools

with open('input.txt') as f:
    data = f.read()


grid = [["#" for _ in range(9)]]


jets = itertools.cycle(data)
pieces = itertools.cycle((
    [
        ["#", "#", "#", "#"]
    ],
    [
        [".", "#", "."],
        ["#", "#", "#"],
        [".", "#", "."]
    ],
    [
        [".", ".", "#"],
        [".", ".", "#"],
        ["#", "#", "#"]
    ],
    [
        ["#"],
        ["#"],
        ["#"],
        ["#"]
    ],
    [
        ["#","#"],
        ["#","#"]
    ]
))


def collision_check(piece, x, y, grid):

    for i in range(len(piece)):
        for j in range(len(piece[0])):
            ch = piece[i][j]
            if ch == "#":
                if grid[y+i][x+j] == "#":
                    return True

    return False


highest_point = 0
i = 0

def draw(piece, x, y, grid):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == '#':
                grid[y+i][x+j] = '#'


points = []
x_positions = []

while i < 30000:
    piece = next(pieces)
    head_room = len(grid) - highest_point - 1
    if len(piece) + 3 >= head_room:
        grid = [["#"] + ['.' for _ in range(7)] + ["#"] for _ in range(len(piece) + 3 - head_room)] + grid
    else:
        grid = grid[head_room - len(piece) - 3:]

    y, x = 0, 3
    while True:
        jet = next(jets)
        if jet == "<":
            x -= 1
            if collision_check(piece, x, y, grid):
                x += 1
        else:
            x += 1
            if collision_check(piece, x, y, grid):
                x -= 1
        
        y += 1
        if collision_check(piece, x, y, grid):
            x_positions.append(x)
            y -= 1
            draw(piece, x, y, grid)
            for ii, row in enumerate(grid):
                if "#" in row[1:-1]:
                    highest_point = len(grid) - ii - 1
                    points.append(highest_point)
                    break
            break

    i += 1

    if i == 2022:
        print("Part 1:", highest_point)


dy = []
for p, pp in zip(points, points[1:]):
    dy.append(pp-p)


s = 20000
for i in range(20,len(dy)):
    if dy[s:s+i] == dy[s+i:s+2*i] == dy[s+2*i:s+3*i]:
        break


pattern = dy[s:s+i]
start = dy[:s]

pattern_sum = sum(pattern)

n = (1000000000000-len(start)) // len(pattern)
remainder = (1000000000000 - len(start)) % len(pattern)

print("Part 2:", n * pattern_sum + sum(start) + sum(pattern[:remainder]))
