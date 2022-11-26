numbers = []
sum = 2020

with open("input.txt") as file:
    for line in file:
        numbers.append(int(line[:-1]))


def part1():
    for n in numbers:
        if (sum - n) in numbers[numbers.index(n) + 1:]:
            print(n*(sum-n))
            break


def part2():
    for n1 in numbers:
        for n2 in numbers[numbers.index(n1) + 1:]:
            if (n1 + n2) <= sum and (sum - n1 - n2) in numbers[numbers.index(n2) + 1:]:
                print(n1 * n2 * (sum - n1 - n2))
                break


# part1()
part2()
