from signal import signal


with open('input.txt') as f:
    data = f.read()


grid  = [["." for _ in range(40)] for _ in range(6)]


def process(grid, clock, x, signal_strengths):
    if clock in (20, 60, 100, 140, 180, 220):
        signal_strengths.append(clock * x)

    row = (clock - 1) // 40
    col = (clock - 1) % 40
    if col in (x - 1, x, x + 1):
        grid[row][col] = "#"


signal_strengths = []
clock = 1
x = 1

for line in data.splitlines():
    if line == 'noop':
        process(grid, clock, x, signal_strengths)
        clock += 1

    else:
        process(grid, clock, x, signal_strengths)
        clock += 1
        process(grid, clock, x, signal_strengths)

        x += int(line.split()[-1])
        clock += 1


print("Part 1:", sum(signal_strengths))
print("Part 2:")
for line in grid:
    print("".join(line))
