from collections import deque
import re

pattern = re.compile(r".*?([A-Z]+).*?(\d+)")

with open('input.txt') as f:
    data = f.read()


data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""



flow_rates = {}
connections = {}
rooms = []
rates = []




for line in data.splitlines():
    f, r = re.match(pattern, line[1:]).groups()

    if 'valves' in line:
        t = line.split('valves ')[1]
        t = tuple(t.split(', '))
    else:
        t = line.split()[-1]
        t = (t,)

    r = int(r)

    flow_rates[f] = r
    connections[f] = t
    rooms.append(f)
    rates.append(r)



rooms2 = []
rates2 = []
for room, rate in zip(rooms, rates):
    if rate != 0:
        rooms2.append(room)
        rates2.append(rate)
    




def shortest_path(r1, r2):
    visited = set()
    path = ()

    q = [(r1, ())]
    q = deque(q)

    while q:
        current, path = q.popleft()

        if current in visited:
            continue
        visited.add(current)

        if current == r2:
            return path + (current,)

        for c in connections[current]:
            q.append((c, path + (current,)))

        
import itertools


shortest_paths = {}
for r1, r2 in itertools.combinations(rooms2, 2):
    shortest_paths[r1, r2] = shortest_path(r1, r2)
    shortest_paths[r2, r1] = shortest_path(r2, r1)




possible_paths = []

q = [("AA", frozenset(), (), 1)]
q = deque(q)

while q:
    current, visited, path, clock = q.popleft()

    if len(path) == len(rooms2):
        possible_paths.append(path)
        continue

    if clock > 30:
        possible_paths.append(path)
        continue

    for r in rooms2:
        if r not in visited:
            l = shortest_path(current, r)
            q.append((r, visited | frozenset([r]), path + (r,), clock + len(l)))



results = []
for path in possible_paths:
    current = "AA"
    clock = 0
    velocity = 0
    pressure = 0

    for room in path:
        l = shortest_path(current, room)
        pressure += velocity * min(30-clock, len(l))
        clock += len(l)
        velocity += flow_rates[room]
        current = room
    
    pressure += max(0, (30 - clock)) * velocity
    results.append((pressure,path))
    

print(max(results))



