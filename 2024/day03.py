import re

report = open('input/day03.txt').read()


# PART 1
pattern = re.compile(r'mul\((\d+),(\d+)\)')

total = 0
for (num1, num2) in re.findall(pattern, report):
    total += int(num1) * int(num2)

print(total)


# PART 2
pattern = re.compile(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))")
list_cmd = []
for text in re.findall(pattern, report):
    list_cmd.append(text)

total = 0
can_add = True
for id, x in enumerate(list_cmd):
    if list_cmd[id] == "do()":
        can_add = True
        continue
    elif list_cmd[id] == "don't()":
        can_add = False
        continue

    if can_add:
        [num1, num2] = list_cmd[id][4:-1].split(',')
        total += int(num1) * int(num2)

print(total)