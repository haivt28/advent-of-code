from copy import deepcopy

report = list(map(str, open('input/day06.txt').read().split('\n')))

map = []
patrol_map = []
obstruction_map = []
patrol_map_advance = [] # map to save directions that have passed => existed mean that's a loop
current_X = 0
current_Y = 0
current_D = 1
direction = {
    1: [-1,  0],    # 1 = North
    2: [ 0,  1],    # 2 = East
    3: [ 1,  0],    # 3 = South
    4: [ 0, -1]     # 4 = West
}

for line in report:
    line = list(line)
    map.append(line)
    patrol_map.append([0] * len(line))
    obstruction_map.append([0] * len(line))
    patrol_map_advance.append([[] for x in range(len(line))])

    if '^' in line:
        current_X = map.index(line)
        current_Y = line.index('^')

first_place_X = current_X
first_place_Y = current_Y
first_place_D = current_D


def check_loop(n_map, c_X, c_Y, c_D):
    pma = deepcopy(patrol_map_advance)

    while True:
        if c_D not in pma[c_X][c_Y]:
            pma[c_X][c_Y].append(c_D)
        else:
            return True

        n_X = c_X + direction[c_D][0]
        n_Y = c_Y + direction[c_D][1]

        if n_X < 0 or n_X >= len(n_map) or n_Y < 0 or n_Y >= len(n_map[c_Y]):
            break

        if n_map[n_X][n_Y] == '#':
            c_D += 1
            if c_D > 4:
                c_D = 1
        else:
            c_X = n_X
            c_Y = n_Y

    return False

while True:
    # PART 1
    # Check the path that the guard visited
    patrol_map[current_X][current_Y] = 1
    next_X = current_X + direction[current_D][0]
    next_Y = current_Y + direction[current_D][1]

    if next_X < 0 or next_X >= len(map) or next_X < 0 or next_Y >= len(map[current_Y]):
        break

    if map[next_X][next_Y] == '#':
        current_D += 1
        if current_D > 4:
            current_D = 1
    else:
        current_X = next_X
        current_Y = next_Y

        # PART 2
        # Simulate new map and check if the guard is stuck in loop
        if not (next_X == first_place_X and next_Y == first_place_Y):
            new_map = deepcopy(map)
            new_map[next_X][next_Y] = '#'
            if check_loop(new_map, first_place_X, first_place_Y, first_place_D):
                obstruction_map[next_X][next_Y] = 1


print(sum(sum(patrol_map,[])))
print(sum(sum(obstruction_map,[])))