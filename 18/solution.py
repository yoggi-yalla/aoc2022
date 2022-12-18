from collections import deque
import itertools

with open('input.txt') as f:
    data = f.read()


# Adding 1 to each pixel index and making the grid slightly larger than the largest
# pixel indexes to ensure that there is room for "air" to surround the droplet

droplet_pixels = [[int(ch) + 1 for ch in line.split(',')] for line in data.splitlines()]

W = max(itertools.chain([p[0] for p in droplet_pixels])) + 2 
D = max(itertools.chain([p[1] for p in droplet_pixels])) + 2
H = max(itertools.chain([p[2] for p in droplet_pixels])) + 2


grid = [[['.' for _ in range(W)] for _ in range(D)] for _ in range(H)]

for x, y, z in droplet_pixels:
    grid[z][y][x] = "#"


def get_surfaces(x, y, z):
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


### Part 1
overlapping_surfaces = set()
droplet_surfaces = set()

for x, y, z in droplet_pixels:
    pixel_surfaces = get_surfaces(x, y, z)
    overlapping_surfaces |= pixel_surfaces & droplet_surfaces
    droplet_surfaces |= pixel_surfaces


hull = droplet_surfaces - overlapping_surfaces
print("Part 1:", len(hull))        


### Part 2
outer_surfaces = set()

q = deque([(0, 0, 0)])
visited = set()

while q:
    x, y, z = q.popleft()

    if (x, y, z) in visited:
        continue
    visited.add((x, y, z))

    for xx, yy, zz in neighbors(x,y,z):
        if grid[zz][yy][xx] == '#':
            outer_surfaces |= droplet_surfaces & get_surfaces(x, y, z)
        else:
            q.append((xx, yy, zz))

print("Part 2:", len(outer_surfaces))


# Prints out all cross sections of the droplet after it has been submerged into the water
'''
for surface in grid:
    print()
    for line in surface:
        print("".join(line))
'''
