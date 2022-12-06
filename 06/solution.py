with open('input.txt') as f:
    data = f.read()


part_1_done = False
for i in range(len(data) - 3):

    if not part_1_done:
        if len(set(data[i:i+4])) == 4:
            print("Part 1:", i + 4)
            part_1_done = True

    
    if len(set(data[i:i+14])) == 14:
        print("Part 2:", i + 14)
        break
