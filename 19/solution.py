from functools import reduce
from operator import add, sub, mul
from collections import deque
import re

with open('input.txt') as f:
    data = f.read()


def strictly_worse(state1, state2):
    _, rocks1, robots1 = state1
    _, rocks2, robots2 = state2

    if (
        all(r1 <= r2 for r1, r2 in zip(rocks1, rocks2)) and
        all(r1 <= r2 for r1, r2 in zip(robots1, robots2))
    ):
        return True
    
    return False


def most_nbr_of_geodes(bp, limit):
    max_ore = max(bp[2], bp[3], bp[5])
    max_clay = bp[4]
    max_obs = bp[6]

    q = deque([(1, (0, 0, 0, 0), (0, 0, 0, 1))])
    visited = set()

    current_clock = 1
    results = []

    # BFS
    while q:
        clock, rocks, robots = q.popleft()


        # When we reach a new depth in the BFS we prune any candidates
        # that are strictly worse than any of the other candidates
        if clock > current_clock:
            current_clock = clock
            qq = deque([])

            for s in q:
                for ss in q:
                    if s is ss:
                        continue
                    if strictly_worse(s, ss):
                        break
                else:
                    qq.append(s)
            q = qq


        if (clock, rocks, robots) in visited:
            continue
        visited.add((clock, rocks, robots))

        if clock > limit:
            results.append(rocks[0])
            continue


        new_rocks = tuple(map(add, rocks, robots))

        if rocks[3] >= bp[5] and rocks[1] >= bp[6]:
            new_rocks_4 = tuple(map(sub, new_rocks, (0,bp[6],0,bp[5])))
            new_robots_4 = tuple(map(add, robots, (1,0,0,0)))
            q.append((clock+1, new_rocks_4, new_robots_4))

            # If it's possible to build a geode robot we don't consider any other alternatives.
            # This is not necessarily true for all inputs...
            continue

        if rocks[3] >= bp[1]:
            if robots[3] < max_ore:
                new_rocks_1 = tuple(map(sub, new_rocks, (0,0,0,bp[1])))
                new_robots_1 = tuple(map(add, robots, (0,0,0,1)))
                q.append((clock+1, new_rocks_1, new_robots_1))

        if rocks[3] >= bp[2]:
            if robots[2] < max_clay:
                new_rocks_2 = tuple(map(sub, new_rocks, (0,0,0,bp[2])))
                new_robots_2 = tuple(map(add, robots, (0,0,1,0)))
                q.append((clock+1, new_rocks_2, new_robots_2))
        
        if rocks[3] >= bp[3] and rocks[2] >= bp[4]:
            if robots[1] < max_obs:
                new_rocks_3 = tuple(map(sub, new_rocks, (0,0,bp[4],bp[3])))
                new_robots_3 = tuple(map(add, robots, (0,1,0,0)))
                q.append((clock+1, new_rocks_3, new_robots_3))
        
        q.append((clock+1, new_rocks, robots))

    return max(results)



### Parse input
pattern = re.compile(r".*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+).*?(\d+)")


blueprints = []

for line in data.splitlines():
    blueprint = tuple(map(int, re.match(pattern, line).groups()))
    blueprints.append(blueprint)



### Part 1
results = []
for bp in blueprints:
    results.append(most_nbr_of_geodes(bp, 24))

print("Part 1:", reduce(add, map(mul, results, range(1,len(blueprints)+1))))



### Part 2
results2 = []
for bp in blueprints[:3]:
    results2.append(most_nbr_of_geodes(bp, 32))

print("Part 2:", reduce(mul, results2))



import time
print(time.process_time()) # 88s ...
