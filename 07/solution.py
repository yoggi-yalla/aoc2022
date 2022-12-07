with open('input.txt') as f:
    data = f.read()


directories = ["/"]
file_to_size = {}

cwd = ""
for line in data.splitlines():
    if line == "$ cd /":
        cwd = "/"

    elif line == "$ cd ..":
        cwd = cwd.rsplit("/", 2)[0] + "/"

    elif line.startswith("$ cd"):
        cwd += line.split()[-1] + "/"
    
    elif line == "$ ls":
        pass
    
    else:
        if line.startswith("dir"):
            directories.append(cwd + line.split()[1])
        else:
            size, name = line.split()
            file_to_size[cwd + name] = int(size)


directory_to_size = {}
for directory in directories:
    size = 0
    for file, s in file_to_size.items():
        if file.startswith(directory):
            size += s
    directory_to_size[directory] = size


total_memory = 70000000
free_memory = total_memory - directory_to_size["/"]
requirement = 30000000 - free_memory


part_1 = sum(v for v in directory_to_size.values() if v <= 100000)
part_2 = min(v for v in directory_to_size.values() if v >= requirement)


print("Part 1:", part_1)
print("Part 2:", part_2)
