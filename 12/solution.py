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


def in_grid(n):
    i, j = n
    if i < 0 or i >= HEIGHT or j < 0 or j >= WIDTH:
        return False
    return True


def neighbors(n):
    i,j = n
    for di, dj in directions:
        ii,jj = i+di, j+dj
        if in_grid((ii,jj)):
            yield (ii,jj)


def run(part_1):
    q = []
    visited = set()

    if part_1:
        q.append((0, start))
    else:
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if grid[i][j] == ord('a'):
                    q.append((0, (i,j)))

    while q:
        cost, current = heapq.heappop(q)

        if current == end:
            break
        
        if current in visited:
            continue
        visited.add(current)

        i,j = current
        for n in neighbors(current):
            ii,jj = n
            if grid[ii][jj] <= 1 + grid[i][j]:
                heapq.heappush(q, (cost + 1, n))
    
    return cost

print("Part 1:", run(True))
print("Part 2:", run(False))
