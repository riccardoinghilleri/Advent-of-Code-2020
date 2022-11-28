def color(string):
    if len(string) == 7 and string[0] == "#":
        for c in string[1:]:
            if 'a' <= c <= 'f' or c.isdigit():
                continue
            else:
                return False
        return True
    return False


def solution(part2=False):
    necessary_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    result = 0
    count = 0
    ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    with open('input.txt') as file:
        for line in file:
            if line != '\n':
                line = line.replace(":", " ")
                line = line.split()
                for i in range(0, len(line), 2):
                    if line[i] in necessary_fields:
                        if part2:
                            if (line[i] == "byr" and 1920 <= int(line[i+1]) <= 2002) \
                                    or (line[i] == "iyr" and 2010 <= int(line[i+1]) <= 2020) \
                                    or (line[i] == "eyr" and 2020 <= int(line[i+1]) <= 2030) \
                                    or (line[i] == "hgt" and ((len(line[i+1]) == 5 and (150 <= int(line[i+1][:3]) <= 193)
                                                               and (line[i+1][3:5] == "cm"))
                                                              or (len(line[i+1]) == 4 and (59 <= int(line[i+1][:2]) <= 76)
                                                                  and (line[i+1][2:4] == "in")))) \
                                    or (line[i] == "hcl" and color(line[i+1])) \
                                    or (line[i] == "ecl" and line[i+1] in ecl) \
                                    or (line[i] == "pid" and len(line[i+1]) == 9 and line[i+1].isdigit()):
                                count += 1
                        else:
                            count += 1
            else:
                if count == 7:
                    result += 1
                count = 0
    if count == 7:
        result += 1
    print(result)


solution(True)
