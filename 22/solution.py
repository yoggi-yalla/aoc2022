import re

with open('input.txt') as f:
    data = f.read()
 

directions = (
    (0,1),
    (1,0),
    (0,-1),
    (-1,0),
)

m, path = data.split('\n\n')


grid = {}
for i,line in enumerate(m.splitlines()):
    for j,ch in enumerate(line):
        if ch != ' ':
            grid[i,j] = ch


max_i = max(grid.keys(), key=lambda x: x[0])[0]
max_j = max(grid.keys(), key=lambda x: x[1])[1]


def next_tile(i,j,dd,part2=False):

    if part2:
        # edge a and left
        if 0<=i<50 and j == 50 and dd == 2:
            return 149-i, 0, 2

        # edge b and up
        if i == 0 and 50<=j<100 and dd == 3:
            return 150 + j%50, 0, 1

        # edge c and up
        if i == 0 and 100<=j<150 and dd == 3:
            return 199, j%50, 0

        # edge d and right
        if 0<=i<50 and j == 149 and dd == 0:
            return 149-i, 99, 2

        # edge e and down
        if i == 49 and 100<=j<150 and dd == 1:
            return 50 + j%50, 99, 1

        # edge f and right
        if 50<=i<100 and j == 99 and dd == 0:
            return 49, 100 + i%50, 3

        # edge g and right
        if 100<=i<150 and j == 99 and dd == 0:
            return 49 - i%50, 149, 2

        # edge h and down
        if i == 149 and 50<=j<100 and dd == 1:
            return 150 + j%50, 49, 1

        # edge i and right
        if 150<=i<200 and j == 49 and dd == 0:
            return 149, 50 + i%50, 3

        # edge j and down
        if i == 199 and 0<=j<50 and dd == 1:
            return 0, 100+j, 0

        # edge k and left
        if 150<=i<200 and j == 0 and dd == 2:
            return 0, 50 + i%50, 3

        # edge l and left
        if 100<=i<150 and j == 0 and dd == 2:
            return 49-i%50, 50, 2

        # edge m and up
        if i == 100 and 0<=j<50 and dd==3:
            return 50 + j%50, 50, 1

        # edge n and left
        if 50<=i<100 and j == 50 and dd==2:
            return 100, i%50, 3

    di, dj = directions[dd]
    ii, jj = i+di, j+dj

    if ii > max_i:
        ii = 0
    if ii < 0:
        ii = max_i
    if jj > max_j:
        jj = 0
    if jj < 0:
        jj = max_j

    while (ii, jj) not in grid:
        ii, jj = ii+di, jj+dj

        if ii > max_i:
            ii = 0
        if ii < 0:
            ii = max_i
        if jj > max_j:
            jj = 0
        if jj < 0:
            jj = max_j

    return ii, jj, 0


def get_password(steps, turns, grid, part2):
    i,j = min(grid.keys())
    dd = 0
    for step, turn in zip(steps, turns):
        for _ in range(step):
            ii, jj, d_inc = next_tile(i,j,dd,part2)
            if grid[ii,jj] == '#':
                break
            else:
                i, j = ii, jj
                dd = (dd + d_inc) % 4

        if turn == 'R':
            dd = (dd + 1) % 4
        elif turn == 'L':
            dd = (dd - 1) % 4
        else:
            pass

    return (i+1) * 1000 + (j+1) * 4 + dd


steps = list(map(int, re.split(r"R|L", path)))
turns = [ch for ch in path if not ch.isdigit()] + ['_']


print("Part 1:", get_password(steps, turns, grid, False))
print("Part 2:", get_password(steps, turns, grid, True))
