with open('input.txt') as f:
    data =f.read()


def make_cycle(nums):
    cycle = {}

    for i in range(1, len(nums)-1):
        cycle[i, nums[i]] = [(i - 1, nums[i - 1]), (i + 1, nums[i + 1])]

    cycle[0, nums[0]] = [(len(nums) - 1, nums[-1]), (1, nums[1])]
    cycle[len(nums) - 1, nums[-1]] = [(len(nums) - 2, nums[-2]), (0, nums[0])]

    return cycle


def swap_forward(cycle, current):
    p = cycle[current][0]
    n = cycle[current][1]
    nn = cycle[n][1]

    cycle[nn][0] = current
    cycle[p][1] = n

    cycle[current][0] = n
    cycle[current][1] = nn

    cycle[n][0] = p
    cycle[n][1] = current


def swap_backward(cycle, current):
    n = cycle[current][1]
    p = cycle[current][0]
    pp = cycle[p][0]

    cycle[pp][1] = current
    cycle[n][0] = p

    cycle[current][0] = pp
    cycle[current][1] = p

    cycle[p][0] = current
    cycle[p][1] = n


def mix(cycle, nums):
    for i, num in enumerate(nums):
        if num % (len(nums) - 1) == 0:
            continue

        current = i, num

        if num > 0:
            for _ in range(num % (len(nums) - 1)):
                swap_forward(cycle, current)
        else:
            for _ in range(-num % (len(nums) - 1)):
                swap_backward(cycle, current)


def grove_coordinates(cycle, nums):
    coords = []
    
    current = nums.index(0), 0
    for i in range(3001):
        if i % 1000 == 0:
            coords.append(current[1])
        current = cycle[current][1]

    return coords



nums1 = [int(x) for x in data.splitlines()]
nums2 = [x * 811589153 for x in nums1]

cycle1 = make_cycle(nums1)
cycle2 = make_cycle(nums2)


mix(cycle1, nums1)
print("Part 1:", sum(grove_coordinates(cycle1, nums1)))


for _ in range(10):
    mix(cycle2, nums2)
print("Part 2:", sum(grove_coordinates(cycle2, nums2)))
