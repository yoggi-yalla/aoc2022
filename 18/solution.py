from collections import defaultdict, deque

with open('input.txt') as f:
    data = f.read()


def get_surfaces(cube):
    x, y, z = cube
    return set([
        frozenset([(x, y, z), (x+1, y, z), (x, y+1, z), (x+1, y+1, z)]),
        frozenset([(x, y, z+1), (x+1, y, z+1), (x, y+1, z+1), (x+1, y+1, z+1)]),

        frozenset([(x, y, z), (x+1, y, z), (x, y, z+1), (x+1, y, z+1)]),
        frozenset([(x, y+1, z), (x+1, y+1, z), (x, y+1, z+1), (x+1, y+1, z+1)]),

        frozenset([(x, y, z), (x, y+1, z), (x, y, z+1), (x, y+1, z+1)]),
        frozenset([(x+1, y, z), (x+1, y+1, z), (x+1, y, z+1), (x+1, y+1, z+1)]),
    ])


directions = (
    ( 1, 0, 0),
    (-1, 0, 0),
    ( 0, 1, 0),
    ( 0,-1, 0),
    ( 0, 0, 1),
    ( 0, 0,-1)
)


def neighbors(x,y,z):
    for dx, dy, dz in directions:
        xx, yy, zz = x+dx, y+dy, z+dz
        if 0 <= xx < W and 0 <= yy < D and 0 <= zz < H:
            yield (xx, yy, zz)



# Parse input
cubes = [[int(ch) + 1 for ch in line.split(',')] for line in data.splitlines()]

max_x = 0
max_y = 0
max_z = 0
for cube in cubes:
    x, y, z = cube
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    max_z = max(z, max_z)


grid = [[['.' for _ in range(max_x+2)] for _ in range(max_y+2)] for _ in range(max_z+2)]

for cube in cubes:
    x, y, z = cube
    grid[z][y][x] = "#"


H = len(grid)
D = len(grid[0])
W = len(grid[0][0])


# Part 1
overlaps = defaultdict(int)
all_surfaces = set()

for cube in cubes:
    surfaces = get_surfaces(cube)
    for s in surfaces:
        if s in all_surfaces:
            overlaps[s] += 1
    all_surfaces |= surfaces

surface_area = len(all_surfaces) - sum(overlaps.values())
print("Part 1:", surface_area)


# Part 2
outer_surfaces = set()

q = [(0,0,0)]
q = deque(q)
visited = set()

while q:
    (x,y,z) = q.popleft()

    if (x,y,z) in visited:
        continue
    visited.add((x,y,z))

    grid[z][y][x] = 'o'

    for xx, yy, zz in neighbors(x,y,z):
        if grid[zz][yy][xx] == '#':
            outer_surfaces |= all_surfaces & get_surfaces((x,y,z))
        else:
            q.append((xx,yy,zz))

print("Part 2:", len(outer_surfaces))


# Prints out all cross sections of the droplet after it has been submerged into the water
'''
for surface in grid:
    print()
    for line in surface:
        print("".join(line))
'''
