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


def get_possible_paths(room, available_rooms, time_limit, current_time=1):
    if not available_rooms:
        return [(room,)]
    
    if current_time >= time_limit:
        return [(room,)]

    possible_paths = []

    for next_room in available_rooms:
        cost = len(shortest_paths[room, next_room])
        p = get_possible_paths(next_room, available_rooms - frozenset([next_room]), time_limit, current_time + cost)
        for pp in p:
            possible_paths.append((room,) + pp)

    return possible_paths


def get_best_result_and_path(possible_paths, shortest_paths, time_limit):
    results = []

    for path in possible_paths:    
        current = path[0]
        clock = 0
        velocity = 0
        pressure = 0

        for room in path[1:]:
            sp = shortest_paths[current, room]
            pressure += velocity * min(time_limit - clock, len(sp))
            clock += len(sp)
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

rooms_with_valves = frozenset(rooms_with_valves)


shortest_paths = {}
for r1, r2 in itertools.combinations(room_map.keys(), 2):
    sp = shortest_path(r1, r2)
    shortest_paths[r1, r2] = sp
    shortest_paths[r2, r1] = sp[::-1]



# Part 1
paths = get_possible_paths("AA", rooms_with_valves, 30)
result, _ = get_best_result_and_path(paths, shortest_paths, 30)

print("Part 1:", result)


# Part 2
best_result = 0
for i in range(1, len(rooms_with_valves) // 2 + 1):
    my_potential_rooms = map(frozenset, itertools.combinations(rooms_with_valves, i))
    for my_rooms in my_potential_rooms:
        my_paths = get_possible_paths("AA", my_rooms, 26)
        my_result, my_path = get_best_result_and_path(my_paths, shortest_paths, 26)

        elephant_paths = get_possible_paths("AA", rooms_with_valves - my_rooms, 26)
        elephant_result, elephant_path = get_best_result_and_path(elephant_paths, shortest_paths, 26)

        best_result = max(best_result, my_result + elephant_result)


print("Part 2:", best_result)


import time
print(time.process_time()) # ~15mins  ¯\_(ツ)_/¯ 
