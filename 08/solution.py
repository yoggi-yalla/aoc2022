with open('input.txt') as f:
    data = f.read()


GRID = [[int(ch) for ch in line] for line in data.splitlines()]

LENGTH = len(GRID)
HEIGHT = len(GRID[0])


directions = (
    ( 0, 1),
    ( 0,-1),
    ( 1, 0),
    (-1, 0)
)


def in_grid(i, j):
    if i < 0 or i >= LENGTH or j < 0 or j >= HEIGHT:
        return False
    return True


def neighbors(i, j, grid):
    for di, dj in directions:
        ns = []

        ii, jj = i + di, j + dj
        while in_grid(ii, jj):
            ns.append(grid[ii][jj])    
            ii, jj = ii + di, jj + dj

        yield ns


def is_visible(i,j, grid):
    if not all((ns for ns in neighbors(i,j,grid))):
        return True

    if any((grid[i][j] > max(ns) for ns in neighbors(i,j,grid))):
        return True

    return False


visible = set()
for i in range(LENGTH):
    for j in range(HEIGHT):
        if is_visible(i, j, GRID):
            visible.add((i,j))

print("Part 1:", len(visible))


scenic_scores = {}
for i in range(LENGTH):
    for j in range(HEIGHT):
        total_score = 1
        for ns in neighbors(i, j, GRID):
            directional_score = 0
            for n in ns:
                directional_score += 1
                if n >= GRID[i][j]:
                    break
            total_score *= directional_score
        scenic_scores[i,j] = total_score

print("Part 2:", max(scenic_scores.values()))
