import copy

input = open('input/day11.txt').read()

# add border (X) to seat map to get rid of checking edge exception
seat_map = []
for line in input.split('\n'):
    seat_map.append(['X'] + list(line) + ['X'])

seat_map.insert(0, ['X'] * (len(seat_map[1])))
seat_map.append(['X'] * (len(seat_map[1])))


def count_one_direction(smap, i, j, x_d, y_d, immediately_adjacent):
    while smap[i][j] != 'X':
        i += x_d
        j += y_d
        if smap[i][j] == '#':
            return 1
        if smap[i][j] == 'L' or immediately_adjacent:
            break
    return 0


def count_adjacent(smap, i, j, immediately_adjacent):
    return \
        count_one_direction(smap, i, j, -1, -1, immediately_adjacent) + \
        count_one_direction(smap, i, j, -1, +0, immediately_adjacent) + \
        count_one_direction(smap, i, j, -1, +1, immediately_adjacent) + \
        count_one_direction(smap, i, j, +0, -1, immediately_adjacent) + \
        count_one_direction(smap, i, j, +0, +1, immediately_adjacent) + \
        count_one_direction(smap, i, j, +1, -1, immediately_adjacent) + \
        count_one_direction(smap, i, j, +1, +0, immediately_adjacent) + \
        count_one_direction(smap, i, j, +1, +1, immediately_adjacent)


def process(current_map, num_occupied_seat, immediately_adjacent):
    while True:
        next_map = copy.deepcopy(current_map)
        is_equal = True
        total_occupied = 0

        for i in range(1, len(current_map) - 1):
            for j in range(1, len(current_map[1]) - 1):
                adjacent_seats = count_adjacent(current_map, i, j, immediately_adjacent)
                if current_map[i][j] == 'L' and adjacent_seats == 0:
                    next_map[i][j] = '#'
                    is_equal = False
                if current_map[i][j] == '#' and adjacent_seats >= num_occupied_seat:
                    next_map[i][j] = 'L'
                    is_equal = False
                if current_map[i][j] == '#':
                    total_occupied += 1

        if is_equal:
            print(total_occupied)
            break

        current_map = next_map


# Part 1
process(seat_map, 4, True)

# Part 2
process(seat_map, 5, False)
