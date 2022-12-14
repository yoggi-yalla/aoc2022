with open('input.txt') as f:
    data = f.read()


grid = [['.' for _ in range(1000)] for _ in range(1000)]


i_max = 0
for line in data.splitlines():
    split = line.split(' -> ')
    i, j = None, None
    for s in split:
        ii, jj = map(int, s.split(',')[::-1])
        i_max = max(i_max, ii)
        
        if (i, j) != (None, None):
            for iii in range(min(i, ii), max(i, ii) + 1):
                for jjj in range(min(j, jj), max(j, jj) + 1):
                    grid[iii][jjj] = '#'

        i, j = ii, jj


floor = i_max + 2
for j in range(len(grid[0])):
    grid[floor][j] = '#'


part_1_done = False
part_2_done = False
counter = 0
while True:
    i, j = (0, 500)
    
    while True:
        if grid[i+1][j] == '.':
            i += 1
        elif grid[i+1][j-1] == '.':
            i += 1
            j -= 1
        elif grid[i+1][j+1] == '.':
            i += 1
            j += 1
        else:
            if grid[i][j] == 'o':
                part_2_done = True
            grid[i][j] = 'o'
            break
    
    if not part_1_done and i > i_max:
        part_1_done = True

        print("Part 1:", counter)

    if part_2_done:
        print("Part 2:", counter)
        break

    counter += 1
