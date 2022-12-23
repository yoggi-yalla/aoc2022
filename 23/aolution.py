from collections import defaultdict

with open('input.txt') as f:
    data = f.read()


north_directions = (
    (-1, -1),
    (-1, 0),
    (-1, 1)
)

south_directions = (
    (1,-1),
    (1,0),
    (1,1)
)

west_directions = (
    (-1, -1),
    (0, -1),
    (1, -1)
)

east_directions = (
    (-1, 1),
    (0, 1),
    (1, 1)
)

sorted_directions = (
    north_directions,
    south_directions,
    west_directions,
    east_directions
)

all_directions = (
    *north_directions, 
    *south_directions,
    *west_directions,
    *east_directions
)


def expand(grid):
    new_grid = []
    new_grid.append(['.']*(len(grid[0])+2))
    for line in grid:
        new_grid.append(['.'] + line + ['.'])
    new_grid.append(['.']*(len(grid[0])+2))
    return new_grid


def find_min_max(grid):
    min_i, min_j = W, H
    max_i, max_j = 0, 0

    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                max_i = max(i, max_i)
                max_j = max(j, max_j)
                min_i = min(i, min_i)
                min_j = min(j, min_j)
    
    return min_i, max_i, min_j, max_j


def count_floor(grid, min_i, max_i, min_j, max_j):
    counter = 0
    for i in range(min_i, max_i+1):
        for j in range(min_j, max_j+1):
            if grid[i][j] == '.':
                counter += 1
    return counter


grid = [[ch for ch in line] for line in data.splitlines()]
H = len(grid)
W = len(grid[0])


dd = 0
counter = 1
while True:
    min_i, max_i, min_j, max_j = find_min_max(grid)

    if min_j == 0 or min_i == 0 or max_i == H-1 or max_j == W-1:
        grid = expand(grid)
        H = len(grid)
        W = len(grid[0])
    
    proposal_counts = defaultdict(int)
    buffer = {}
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                for di, dj in all_directions:
                    if grid[i+di][j+dj] == '#':
                        break
                else:
                    continue
                
                for ii in range(4):
                    ddd = (dd + ii) % 4
                    ddi, ddj = sorted_directions[ddd][1]
                    for di, dj in sorted_directions[ddd]:
                        if grid[i+di][j+dj] == '#':
                            break
                    else:
                        proposal_counts[i+ddi, j+ddj] += 1
                        buffer[i,j] = (i+ddi, j+ddj)
                        break


    for (i,j),(ii,jj) in buffer.items():
        if proposal_counts[ii,jj] > 1:
            continue
        grid[i][j] = '.'
        grid[ii][jj] = '#'

    dd = (dd+1) % 4

    if counter == 10:
        min_i, max_i, min_j, max_j = find_min_max(grid)
        print("Part 1:", count_floor(grid, min_i, max_i, min_j, max_j))

    if len(buffer) == 0:
        print("Part 2:", counter)
        break

    counter += 1
