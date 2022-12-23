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


elves = set()
for i, line in enumerate(data.splitlines()):
    for j, ch in enumerate(line):
        if ch == '#':
            elves.add((i, j))


d = 0
round = 0
while True:
    proposals = {}
    proposal_counter = defaultdict(int)

    for (i, j) in elves:
        for di, dj in all_directions:
            ii, jj = i + di, j + dj
            if (ii, jj) in elves:
                break
        else:
            continue

        for inc in range(4):
            dd = (d + inc) % 4
            for di, dj in sorted_directions[dd]:
                ii, jj = i + di, j + dj
                if (ii, jj) in elves:
                    break
            else:
                di, dj = sorted_directions[dd][1]
                ii, jj = i + di, j + dj
                proposals[i, j] = ii, jj
                proposal_counter[ii, jj] += 1
                break
        
    for k, v in proposals.items():
        if proposal_counter[v] > 1:
            continue
        elves.remove(k)
        elves.add(v)


    if round == 10:
        min_i = min(e[0] for e in elves)
        max_i = max(e[0] for e in elves)
        min_j = min(e[1] for e in elves)
        max_j = max(e[1] for e in elves)

        print("Part 1:", (max_i - min_i) * (max_j - min_j) - len(elves))


    if len(proposals) == 0:
        print("Part 2:", round + 1)
        break
    
    d = (d + 1) % 4
    round += 1
