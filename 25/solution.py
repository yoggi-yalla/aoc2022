with open('input.txt') as f:
    data = f.read()


def count(s):
    p = 0
    c = 0
    for ch in s[::-1]:
        if ch == '=':
            n = -2
        elif ch == '-':
            n = -1
        else:
            n = int(ch)
        c += n * (5 ** p)
        p += 1
    return c


counter = 0
for line in data.splitlines():
    counter += count(line)


nums = "210-="


guess = "2" * 20
for i in range(len(guess)):
    for j in range(5):
        new_guess = guess[:i] + nums[j] + guess[i+1:]
        if count(new_guess) >= counter:
            guess = new_guess


print("Part 1 & 2:", guess)
