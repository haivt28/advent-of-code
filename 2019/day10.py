import math


def is_between(a, c, b):
    is_between_x = False
    if a[0] >= b[0]:
        if a[0] >= c[0] >= b[0]:
            is_between_x = True
    else:
        if a[0] <= c[0] <= b[0]:
            is_between_x = True

    is_between_y = False
    if a[1] >= b[1]:
        if a[1] >= c[1] >= b[1]:
            is_between_y = True
    else:
        if a[1] <= c[1] <= b[1]:
            is_between_y = True

    return is_between_x and is_between_y


def collinear(a, b, c):
    x = a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])
    if x == 0:
        return True
    return False


def angle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    return ang + 360 if ang < 0 else ang


input = '''###..#########.#####.
.####.#####..####.#.#
.###.#.#.#####.##..##
##.####.#.###########
###...#.####.#.#.####
#.##..###.########...
#.#######.##.#######.
.#..#.#..###...####.#
#######.##.##.###..##
#.#......#....#.#.#..
######.###.#.#.##...#
####.#...#.#######.#.
.######.#####.#######
##.##.##.#####.##.#.#
###.#######..##.#....
###.##.##..##.#####.#
##.########.#.#.#####
.##....##..###.#...#.
#..#.####.######..###
..#.####.############
..##...###..#########'''
asteroids = []
x = 0
y = 0
for i in input:
    if i == '#':
        asteroids.append((x, y))
    x += 1
    if i == '\n':
        x = 0
        y += 1
print(asteroids)
detect = [0] * len(asteroids)
direct_list = [[] for _ in range(len(asteroids))]

for i in range(0, len(asteroids)):
    for j in range(0, len(asteroids)):
        if i != j:
            direct = True
            for k in range(0, len(asteroids)):
                if i != k != j and is_between(asteroids[i], asteroids[k], asteroids[j]):
                    if collinear(asteroids[i], asteroids[k], asteroids[j]):
                        direct = False
                        break
            if direct:
                detect[i] += 1
                (direct_list[i]).append(asteroids[j])

print(max(detect))
max_id = detect.index(max(detect))
print(asteroids[max_id])

direct = direct_list[max_id]
angles = []
point1 = (asteroids[max_id][0], asteroids[max_id][1] - 10)
point2 = asteroids[max_id]
for point3 in direct:
    angles.append(angle(point1, point2, point3))

sorted_direct = [x for _,x in sorted(zip(angles, direct))]
print(sorted_direct[199])
