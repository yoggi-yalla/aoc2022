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
actual_goal = (goal[0]+1,goal[1])



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



i = 0
all_blizzards = {}
all_blizzards[i] = grid
all_blizzards_set = set([grid])

new_grid = next_grid(grid)
while True:
    i += 1
    if new_grid in all_blizzards_set:
        break
    all_blizzards[i] = new_grid
    all_blizzards_set.add(new_grid)

    new_grid = next_grid(new_grid)

nbr_blizzards = len(all_blizzards)



def neighbors(state):
    time, pos, _ = state
    i, j = pos
    options = []

    new_grid = all_blizzards[(time+1)%nbr_blizzards]

    if pos == actual_start:
        options.append((time+1, (i,j), new_grid))
        if new_grid[0][0] == EMPTY:
            options.append((time+1, (0,0), new_grid))
        return options

    if pos == actual_goal:
        options.append((time+1, (i,j), new_grid))
        ii,jj = goal
        if new_grid[ii][jj] == EMPTY:
            options.append((time+1, (ii,jj), new_grid))
        return options

    if new_grid[i][j] == EMPTY:
        options.append((time+1, (i, j), new_grid))
    
    if j > 0:
        if new_grid[i][j-1] == EMPTY:
            options.append((time+1, (i,j-1), new_grid))

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

    return time + 1

t1 = run(actual_start, goal, grid, 0)
t2 = run(actual_goal, start, grid, t1)
t3 = run(actual_start, goal, grid, t2)

print("Part 1:", t1)
print("Part 2:", t3)
