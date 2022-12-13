from functools import cmp_to_key

with open('input.txt') as f:
    data = f.read()


def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        if left == right:
            return 0
        if left > right:
            return -1
    
    if type(left) == list and type(right) == list:
        for l, r in zip(left, right):
            c = compare(l, r)

            if c == 1:
                return 1
            if c == -1:
                return -1

        if len(left) == len(right):
            return 0
        if len(left) < len(right):
            return 1
        if len(left) > len(right):
            return -1
    
    if type(left) == int:
        return compare([left], right)
    
    if type(right) == int:
        return compare(left, [right])


correct_pairs = 0
packets = []
for i, group in enumerate(data.split('\n\n')):
    left, right = group.splitlines()
    left, right = eval(left), eval(right)

    packets.append(left)
    packets.append(right)

    if compare(left, right) in (0, 1):
        correct_pairs += i + 1

print("Part 1:", correct_pairs)


packets.append([[2]])
packets.append([[6]])
packets.sort(key=cmp_to_key(compare), reverse=True)
decoder_key = (packets.index([[2]])+1) * (packets.index([[6]])+1)

print("Part 2:", decoder_key)
