input = open('input/day12.txt').read()


# PART 1
directions = ['E', 'S', 'W', 'N']
facing = 'E'
current_point = [0, 0]

for line in input.split('\n'):
    direction = line[0]
    num = int(line.replace(line[0], ''))

    if direction == 'L':
        cur_index = directions.index(facing) - num // 90
        facing = directions[cur_index % len(directions)]
    elif direction == 'R':
        cur_index = directions.index(facing) + num // 90
        facing = directions[cur_index % len(directions)]
    elif direction == 'N' or (direction == 'F' and facing == 'N'):
        current_point[1] += num
    elif direction == 'S' or (direction == 'F' and facing == 'S'):
        current_point[1] -= num
    elif direction == 'W' or (direction == 'F' and facing == 'W'):
        current_point[0] -= num
    elif direction == 'E' or (direction == 'F' and facing == 'E'):
        current_point[0] += num

print(abs(current_point[0]) + abs(current_point[1]))


# PART 2
# Solution 1: Use normal rotation
current_point = [0, 0]
waypoint = [10, 1]

for line in input.split('\n'):
    direction = line[0]
    num = int(line.replace(line[0], ''))

    wp0 = waypoint[0]
    wp1 = waypoint[1]

    if (direction == 'L' and num == 90) or (direction == 'R' and num == 270):
        waypoint[0] = -wp1
        waypoint[1] = wp0
    elif num == 180:
        waypoint[0] = -wp0
        waypoint[1] = -wp1
    if (direction == 'L' and num == 270) or (direction == 'R' and num == 90):
        waypoint[0] = wp1
        waypoint[1] = -wp0
    elif direction == 'N':
        waypoint[1] += num
    elif direction == 'S':
        waypoint[1] -= num
    elif direction == 'W':
        waypoint[0] -= num
    elif direction == 'E':
        waypoint[0] += num
    elif direction == 'F':
        current_point[0] += num * waypoint[0]
        current_point[1] += num * waypoint[1]

print(abs(current_point[0]) + abs(current_point[1]))

# Solution 2: Use complex number
# Ref: https://betterexplained.com/articles/a-visual-intuitive-guide-to-imaginary-numbers/
current_point = complex(0, 0)
waypoint = complex(10, 1)

for line in input.split('\n'):
    direction = line[0]
    num = int(line.replace(line[0], ''))

    if direction == 'L':
        waypoint *= complex(0, 1) ** (num // 90)
    if direction == 'R':
        waypoint *= complex(0, -1) ** (num // 90)
    elif direction == 'N':
        waypoint += complex(0, num)
    elif direction == 'S':
        waypoint += complex(0, -num)
    elif direction == 'W':
        waypoint += complex(-num, 0)
    elif direction == 'E':
        waypoint += complex(num, 0)
    elif direction == 'F':
        current_point += num * waypoint

print(abs(current_point.real) + abs(current_point.imag))
