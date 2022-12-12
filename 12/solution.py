import heapq

with open('input.txt') as f:
    data = f.read()


grid = []
for i, line in enumerate(data.splitlines()):
    row = []
    for j, ch in enumerate(line):
        if ch == 'S':
            start = (i, j)
            ch = 'a'
        if ch == 'E':
            end = (i, j)
            ch = 'z'
        row.append(ord(ch))
    grid.append(row)


HEIGHT = len(grid)
WIDTH = len(grid[0])


directions = (
    ( 0, 1),
    ( 0,-1),
    ( 1, 0),
    (-1, 0)
)


def neighbors(i, j):
    for di, dj in directions:
        ii, jj = i + di, j + dj
        if 0 <= ii < HEIGHT and 0 <= jj < WIDTH:
            yield (ii, jj)


def run(part_1):
    q = []
    visited = set()

    if part_1:
        q.append((0, start))
    else:
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if grid[i][j] == ord('a'):
                    q.append((0, (i, j)))

    while q:
        cost, (i, j) = heapq.heappop(q)

        if (i, j) == end:
            break
        
        if (i, j) in visited:
            continue
        visited.add((i, j))

        for ii, jj in neighbors(i, j):
            if grid[ii][jj] <= 1 + grid[i][j]:
                heapq.heappush(q, (cost + 1, (ii, jj)))
    
    return cost

print("Part 1:", run(True))
print("Part 2:", run(False))
