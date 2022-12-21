with open('input.txt') as f:
    data = f.read()


def resolve(name, nodes):
    if name not in nodes:
        return int(name)

    c = nodes[name]

    if len(c) == 1:
        return resolve(c[0], nodes)

    r1 = resolve(c[0], nodes)
    r2 = resolve(c[2], nodes)

    op = c[1]

    if op == '+':
        return r1 + r2
    elif op == '-':
        return r1 - r2
    elif op == '*':
        return r1 * r2
    elif op == '/':
        return r1 / r2

    else:
        raise ValueError('Invalid input!')


def sign(x):
    return x // abs(x)


def binary_search(f, lower, upper):
    l_value = f(lower)
    u_value = f(upper)

    if sign(l_value) == sign(u_value):
        raise ValueError(f"The range [{lower}, {upper}] does not contain zero")

    if l_value > u_value:
        ff = lambda x: -f(x)
    else:
        ff = f

    while lower <= upper:
        mid = (lower + upper) // 2
        m_value = ff(mid)

        if m_value == 0:
            return mid

        elif m_value < 0:
            lower = mid + 1

        else:
            upper = mid

    return lower


def find_root_equality(nodes):
    left = nodes['root'][0]
    right = nodes['root'][2]

    def goal_seek_function(human_input):
        nodes['humn'] = [str(human_input)]
        return resolve(left, nodes) - resolve(right, nodes)
    
    return binary_search(goal_seek_function, 1, int(1e15))


nodes = {}

for line in data.splitlines():
    name, op = line.split(': ')
    nodes[name] = op.split()


print("Part 1:", int(resolve('root', nodes)))
print("Part 2:", find_root_equality(nodes))


import time
print(time.process_time()) # <0.1s
