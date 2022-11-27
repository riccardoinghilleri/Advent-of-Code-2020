initial = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
slopes = [1, 3, 5, 7, 1]
trees = [0, 0, 0, 0, 0]
jump = True
mult = 1
lastmult = 1
with open('input.txt') as file:
    for line in file:
        if not jump:
            line = line[:-1]
            for index in range(len(slopes) - 1):
                if line[slopes[index] % len(line)] == "#":
                    trees[index] += 1
                slopes[index] = (slopes[index] + initial[index][0]) % len(line)
            if mult % 2 == 0:
                if line[slopes[4] % len(line)] == "#":
                    trees[4] += 1
                slopes[4] = (slopes[4] + initial[4][0]) % len(line)
            mult += 1
        else:
            jump = False
count = 1
for elem in trees:
    count *= elem
print(trees[1])
print(count)
