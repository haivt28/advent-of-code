import copy


def count_neighbour(layers, x, y, z, w):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                        count += int(layers[w + dw][z + dz][x + dx][y + dy] == '#')
    return count


def count_active(num_cycle, core, has_w_dim=False):
    dim_len = (num_cycle + 1) * 2 + 1
    w_dim_len = dim_len if has_w_dim else 3
    pocket = [[[['.' for _ in range(dim_len + len(core) - 1)] for _ in range(dim_len + len(core) - 1)] for _ in range(dim_len)] for _ in range(w_dim_len)]
    for x in range(len(core)):
        for y in range(len(core[x])):
            mid = dim_len // 2
            mid4 = len(pocket) // 2
            pocket[mid4][mid][mid + x][mid + y] = core[x][y]

    for cycle in range(num_cycle):
        next_state = copy.deepcopy(pocket)
        active_count = 0
        for w in range(1, len(pocket) - 1):
            for z in range(1, len(pocket[w]) - 1):
                for x in range(1, len(pocket[w][z]) - 1):
                    for y in range(1, len(pocket[w][z][x]) - 1):
                        current = pocket[w][z][x][y]
                        count = count_neighbour(pocket, x, y, z, w)

                        if current == '#' and count != 2 and count != 3:
                            next_state[w][z][x][y] = '.'
                        elif current == '.' and count == 3:
                            next_state[w][z][x][y] = '#'
                        else:
                            next_state[w][z][x][y] = current

                        if next_state[w][z][x][y] == '#':
                            active_count += 1

        pocket = copy.deepcopy(next_state)
        if cycle == num_cycle - 1:
            print(active_count)


input = open('input/day17.txt').read()

num_cycle = 6
core = []
for line in input.split('\n'):
    core.append(list(line))

# PART 1
count_active(num_cycle, core, has_w_dim=False)

# PART 2
count_active(num_cycle, core, has_w_dim=True)
