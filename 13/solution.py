from functools import cmp_to_key

with open('input.txt') as f:
    data = f.read()


def compare_literal(left, right):
    if left < right:
        return -1
    if left == right:
        return  0
    if left > right:
        return  1


def compare(left, right):
    l_type = type(left)
    r_type = type(right)

    if (l_type, r_type) == (int, int):
        return compare_literal(left, right)

    elif (l_type, r_type) == (list, list):
        for l, r in zip(left, right):
            if (c := compare(l, r)) != 0:
                return c

        return compare_literal(len(left), len(right))

    elif (l_type, r_type) == (int, list):
        return compare([left], right)

    elif (l_type, r_type) == (list, int):
        return compare(left, [right])

    else:
        raise ValueError("Invalid input!")


correct_pairs = 0
packets = []
for i, group in enumerate(data.split('\n\n')):
    left, right = group.splitlines()
    left, right = eval(left), eval(right)

    packets.append(left)
    packets.append(right)

    if compare(left, right) in (0, -1):
        correct_pairs += i + 1

print("Part 1:", correct_pairs)


packets.append([[2]])
packets.append([[6]])
packets.sort(key=cmp_to_key(compare))
decoder_key = (packets.index([[2]])+1) * (packets.index([[6]])+1)

print("Part 2:", decoder_key)
