input = open('input/day02.txt').read()

# PART 1
valid_count = 0

for line in input.split('\n'):
    line = line.split()
    min_appear = int(line[0].split('-')[0])
    max_appear = int(line[0].split('-')[1])
    appear = line[2].count(line[1][0])
    # print(min_appear, max_appear, appear)
    if min_appear <= appear <= max_appear:
        valid_count += 1

print(valid_count)

# PART 2
valid_count = 0
for line in input.split('\n'):
    line = line.split()
    first_idx = int(line[0].split('-')[0]) - 1
    second_idx = int(line[0].split('-')[1]) - 1
    char = line[1][0]
    string = line[2]
    # print(string[first_idx], string[second_idx])
    if (int(string[first_idx] == char) + int(string[second_idx] == char)) == 1:
        valid_count += 1

print(valid_count)
