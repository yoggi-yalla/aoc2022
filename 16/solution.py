from collections import deque
import itertools
import re

with open('input.txt') as room:
    data = room.read()


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

        for c in room_map[current]:
            q.append((c, path + (current,)))


def get_possible_paths(available_rooms, time_limit):
    possible_paths = []

    q = [("AA", frozenset(), (), 1)]
    q = deque(q)

    while q:
        current, visited, path, clock = q.popleft()

        if len(path) == len(available_rooms):
            possible_paths.append(path)
            continue

        if clock >= time_limit:
            possible_paths.append(path)
            continue

        for rate in available_rooms:
            if rate not in visited:
                l = shortest_path(current, rate)
                q.append((rate, visited | frozenset([rate]), path + (rate,), clock + len(l)))
    
    return possible_paths


def get_best_result_and_path(possible_paths, time_limit):
    results = []

    for path in possible_paths:    
        current = "AA"
        clock = 0
        velocity = 0
        pressure = 0

        for room in path:
            l = shortest_path(current, room)
            pressure += velocity * min(time_limit - clock, len(l))
            clock += len(l)
            velocity += flow_rates[room]
            current = room
        
        pressure += max(0, (time_limit - clock)) * velocity
        results.append((pressure, path))
    
    return max(results)


# Parse input
flow_rates = {}
room_map = {}
rooms_with_valves = []

for line in data.splitlines():

    room = line.split()[1]
    rate = int(re.match(r".*?(\d+)", line).groups()[0])
    connections = tuple(re.split(r"valves? ", line)[1].split(', '))

    flow_rates[room] = rate
    room_map[room] = connections

    if rate > 0:
        rooms_with_valves.append(room)


shortest_paths = {}
for r1, r2 in itertools.combinations(rooms_with_valves, 2):
    sp = shortest_path(r1, r2)
    shortest_paths[r1, r2] = sp
    shortest_paths[r2, r1] = sp[::-1]


# Part 1
paths = get_possible_paths(rooms_with_valves, 30)
result, _ = get_best_result_and_path(paths, 30)

print("Part 1:", result)


# Part 2
my_paths = get_possible_paths(rooms_with_valves, 26)
my_result, my_rooms = get_best_result_and_path(my_paths, 26)


elephant_rooms = [r for r in rooms_with_valves if r not in my_rooms]
elephant_paths = get_possible_paths(elephant_rooms, 26)

elephant_result, elephant_path = get_best_result_and_path(elephant_paths, 26)


print("Part 2:", my_result + elephant_result)


import time
print(time.process_time()) # ~3mins  ¯\_(ツ)_/¯ 
