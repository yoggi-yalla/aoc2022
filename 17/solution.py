import itertools

with open('input.txt') as f:
    data = f.read()


grid = [["#" for _ in range(9)]]


jets = itertools.cycle(enumerate(data))
pieces = itertools.cycle(enumerate((
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
)))


def collision_check(piece, x, y, grid):

    for i in range(len(piece)):
        for j in range(len(piece[0])):
            ch = piece[i][j]
            if ch == "#":
                if grid[y+i][x+j] == "#":
                    return True

    return False


def insert(piece, x, y, grid):
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == '#':
                grid[y+i][x+j] = '#'


def add_space_above(grid, n_rows):
    return [["#"] + ['.' for _ in range(7)] + ["#"] for _ in range(n_rows)] + grid


states = {}
highest_points = [0]


i = 0
pattern_found = False

while True:
    piece_index, piece = next(pieces)

    space_above = len(grid) - highest_points[-1] - 1
    space_needed = len(piece) + 3

    rows_required = space_needed - space_above

    if rows_required >= 0:
        grid = add_space_above(grid, rows_required)
    else:
        grid = grid[-rows_required:]

    y, x = 0, 3
    while True:
        jet_index, jet = next(jets)
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
            y -= 1
            insert(piece, x, y, grid)
            for ii, row in enumerate(grid):
                if "#" in row[1:-1]:
                    highest_points.append(len(grid) - ii - 1)
                    break
            break

    state = (jet_index, piece_index, "".join(itertools.chain(*grid[:30])))

    if state in states and not pattern_found:
        pattern_start, pattern_end = states[state], i
        pattern_found = True

    states[state] = i

    i += 1
    
    if i == 2022:
        print("Part 1:", highest_points[-1]) # 3102
    
    if i >= 2022 and pattern_found:
        break


d_height = [hh - h for h, hh in zip(highest_points, highest_points[1:])]


pattern = d_height[pattern_start:pattern_end]
start_seq = d_height[:pattern_start]


n = (1000000000000 - len(start_seq)) // len(pattern)
remainder = (1000000000000 - len(start_seq)) % len(pattern)

print("Part 2:", sum(start_seq) + n * sum(pattern) + sum(pattern[:remainder]))
