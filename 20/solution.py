with open('input.txt') as f:
    data =f.read()


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


def connect(nodes):
    for n1, n2 in zip(nodes, nodes[1:]):
        n1.next = n2
        n2.prev = n1
    
    nodes[0].prev = nodes[-1]
    nodes[-1].next = nodes[0]


def mix(nodes, iterations=1):
    for _ in range(iterations):
        for node in nodes:

            n = node.next
            p = node.prev

            p.next = n
            n.prev = p

            for _ in range(node.value % (len(nodes) - 1)):
                p, n = n, n.next

            p.next = node
            n.prev = node

            node.next = n
            node.prev = p


def grove_coordinates(nodes):
    coords = []
    for n in nodes:
        if n.value == 0:
            for _ in range(3):
                for _ in range(1000):
                    n = n.next
                coords.append(n.value)
            break
    return coords


nodes1 = [Node(int(x)) for x in data.splitlines()]
connect(nodes1)
mix(nodes1)
print("Part 1:", sum(grove_coordinates(nodes1)))


nodes2 = [Node(int(x) * 811589153) for x in data.splitlines()]
connect(nodes2)
mix(nodes2, 10)
print("Part 2:", sum(grove_coordinates(nodes2)))
