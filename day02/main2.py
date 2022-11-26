count = 0
with open('input.txt') as file:
    for line in file:
        line = line.replace(":", "")
        line = line.replace("-", " ")
        line = line.split()
        if (line[3][int(line[0]) - 1] == line[2] and line[3][int(line[1]) - 1] != line[2]) \
                or (line[3][int(line[0]) - 1] != line[2] and line[3][int(line[1]) - 1] == line[2]):
            count += 1

print(count)
