input = open('input/day03.txt').read()

# PART 1
current_idx = 0
tree_count = 0

for line in input.split('\n'):
    # print(line)
    if current_idx > len(line) - 1:
        current_idx -= len(line)
    if line[current_idx] == '#':
        tree_count += 1
    # print(' '*current_idx + line[current_idx])
    current_idx += 3

print(tree_count)

# PART 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result = 1
input_arr = input.split('\n')

for slope in slopes:
    current_idx = 0
    tree_count = 0
    i = 0
    while i < len(input_arr):
        line = input_arr[i]
        if current_idx > len(line) - 1:
            current_idx -= len(line)
        if line[current_idx] == '#':
            tree_count += 1
        current_idx += slope[0]
        i += slope[1]

    # print(tree_count)
    result *= tree_count

print(result)
