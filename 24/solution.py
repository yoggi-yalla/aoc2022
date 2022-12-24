import heapq

with open('input.txt') as f:
    data = f.read()

EMPTY = ('.',)


grid = [[[ch] for ch in line[1:-1]] for line in data.splitlines()[1:-1]]

H = len(grid)
W = len(grid[0])

for i in range(H):
    for j in range(W):
        if grid[i][j] != ['.']:
            grid[i][j] = ['.'] + grid[i][j] 

grid = tuple(tuple(tuple(sorted(spot)) for spot in row) for row in grid)


start = (0, 0)
goal = (len(grid)-1, len(grid[0])-1)

actual_start = (-1, 0)
actual_goal = (goal[0] + 1, goal[1])


def next_grid(grid):
    new_grid = [[['.'] for _ in row] for row in grid]

    for i, row in enumerate(grid):
        for j, spot in enumerate(row):
            for e in spot:
                if e == '^':
                    new_grid[(i-1)%H][j].append('^')
                elif e == '>':
                    new_grid[i][(j+1)%W].append('>')
                elif e == 'v':
                    new_grid[(i+1)%H][j].append('v')
                elif e == '<':
                    new_grid[i][(j-1)%W].append('<')
    
    return tuple(tuple(tuple(sorted(spot)) for spot in row) for row in new_grid)


def get_all_grids(grid):
    all_grids = {0: grid}
    all_grids_set = set([grid])

    i = 1
    while True:
        grid = next_grid(grid)
        if grid in all_grids_set:
            break

        all_grids[i] = grid
        all_grids_set.add(grid)

        i += 1

    return all_grids, len(all_grids)


all_grids, nbr_grids = get_all_grids(grid)


def neighbors(state):
    time, pos, _ = state
    i, j = pos
    options = []

    new_grid = all_grids[(time+1)%nbr_grids]

    if pos == actual_start:
        options.append((time+1, (i, j), new_grid))
        if new_grid[0][0] == EMPTY:
            options.append((time+1, (0, 0), new_grid))
        return options

    if pos == actual_goal:
        options.append((time+1, (i, j), new_grid))
        ii, jj = goal
        if new_grid[ii][jj] == EMPTY:
            options.append((time+1, (ii, jj), new_grid))
        return options

    if new_grid[i][j] == EMPTY:
        options.append((time+1, (i, j), new_grid))
    
    if j > 0:
        if new_grid[i][j-1] == EMPTY:
            options.append((time+1, (i, j-1), new_grid))

    if i > 0:
        if new_grid[i-1][j] == EMPTY:
            options.append((time+1, (i-1, j), new_grid))
    
    if j < W - 1:
        if new_grid[i][j+1] == EMPTY:
            options.append((time+1, (i, j+1), new_grid))
    
    if i < H - 1:
        if new_grid[i+1][j] == EMPTY:
            options.append((time+1, (i+1, j), new_grid))
    
    return options


def min_cost(pos, goal):
    i, j = pos
    ii, jj = goal
    return (abs(i-ii) + abs(j-jj))


def run(start, goal, grid, time):

    start_state = (0, time, start, grid)
    q = [start_state]
    visited = set()

    while q:
        _, time, pos, grid = heapq.heappop(q)

        if (pos, grid) in visited:
            continue
        visited.add((pos, grid))

        if pos == goal:
            break

        for tt, pp, gg in neighbors((time, pos, grid)):
            if (pp, gg) in visited:
                continue
            ec = tt + min_cost(pp, goal)
            heapq.heappush(q, (ec, tt, pp, gg))

    time += 1
    grid = next_grid(grid)

    return time, grid


t1, g1 = run(actual_start, goal, grid, 0)
t2, g2 = run(actual_goal, start, g1, t1)
t3, g3 = run(actual_start, goal, g2, t2)

print("Part 1:", t1)
print("Part 2:", t3)
