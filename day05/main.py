import math


def find(string, final_value):  # 32 47
    start_value = 0
    for c in string:
        if c == 'L' or c == 'F':
            final_value = start_value + math.floor((final_value - start_value) / 2)
        else:
            start_value += (math.floor((final_value - start_value) / 2) + 1)
    return final_value


seats_list = []
my_seat = -1
with open('input.txt') as file:
    for line in file:
        row = find(line[:7], 127)
        column = find(line[7:10], 7)
        seats_list.append(row * 8 + column)
seats_list.sort()
for i in range(1, len(seats_list)):
    if seats_list[i] != seats_list[i-1] + 1:
        my_seat = seats_list[i] - 1
        break
print(max(seats_list))
print(my_seat)
