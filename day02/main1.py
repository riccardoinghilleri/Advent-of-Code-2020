count = 0
with open('input.txt') as file:
    for line in file:
        line = line.replace(":", "")
        line = line.replace("-", " ")
        line = line.split()
        if int(line[0]) <= line[3].count(line[2]) <= int(line[1]):
            count += 1

print(count)
