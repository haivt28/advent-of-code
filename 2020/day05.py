input = open('input/day05.txt').read()


def calculate_seat_id(binary_str):
    current_row = 127
    index = 0
    for i in reversed(range(7)):
        index += 1
        if binary_str[index] == '0':
            current_row -= pow(2, i)

    current_col = 7
    for i in reversed(range(3)):
        index += 1
        if binary_str[index] == '0':
            current_col -= pow(2, i)

    return current_row * 8 + current_col


# PART 1
max_val = 0
max_binary = ''
for line in input.split('\n'):
    line = line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
    line = '1' + line
    if int(line, 2) > max_val:
        max_val = int(line, 2)
        max_binary = line

print(calculate_seat_id(max_binary))


# PART 2
all_ids = []
for line in input.split('\n'):
    line = line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
    line = '1' + line
    all_ids.append(calculate_seat_id(line))

start = 0
all_ids = sorted(all_ids)
for i in range(min(all_ids), max(all_ids) + 1):
    if i != all_ids[start]:
        print(i)
        break
    start += 1
