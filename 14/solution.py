from collections import defaultdict

with open('input.txt') as f:
    data = f.read()


grid = [['.' for _ in range(1000)] for _ in range(1000)]


i_max = 0
for line in data.splitlines():
    split = line.split(' -> ')
    i,j = None, None
    for s in split:
        ii, jj = int(s.split(',')[1]), int(s.split(',')[0])
        i_max = max(i_max, ii)
        
        if (i,j) != (None, None):
            if ii != i:
                if i < ii:
                    for iii in range(i, ii+1):
                        grid[iii][jj] = '#'
                else:
                    for iii in range(ii, i + 1):
                        grid[iii][jj] = '#'
            else:
                if j < jj:
                    for jjj in range(j, jj+1):
                        grid[ii][jjj] = '#'
                else:
                    for jjj in range(jj, j+1):
                        grid[ii][jjj] = '#'

        i,j = ii, jj


for jj in range(len(grid[0])):
    grid[i_max+2][jj] = '#'

broken = False
counter = 0
while True:
    counter += 1
    i,j = (0, 500)

    if grid[i][j] == 'o':
        break
    
    while True:
        if grid[i+1][j] == '.':
            i += 1
            continue
        if grid[i+1][j-1] == '.':
            i += 1
            j -= 1
            continue
        if grid[i+1][j+1] == '.':
            i += 1
            j += 1
            continue
        else:
            if grid[i][j] == 'o':
                broken = True
            grid[i][j] = 'o'
            break
    
    if broken:
        break


print(counter-1)
