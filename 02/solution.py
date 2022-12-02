with open('input.txt') as f:
    data = f.read()


points = {
    'A': 1,
    'B': 2,
    'C': 3
}

winning_move = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

losing_move = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

translation = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}


score = 0
for line in data.splitlines():
    you, me = line.split()
    me = translation[me]

    if you == me:
        score += 3
    if winning_move[you] == me:
        score += 6
    
    score += points[me]

print("Part 1:", score)


score = 0
for line in data.splitlines():
    you, me = line.split()
    
    if me == 'X':
        me = losing_move[you]
    if me == 'Y':
        me = you
        score += 3
    if me == 'Z':
        me = winning_move[you]
        score += 6

    score += points[me]

print("Part 2:", score)
