data = list(open('input/day03.txt').read().split())

path = [data[0].split(','), data[1].split(',')]

# Testcases
# path = [['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
#         ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]
#
# path = [['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
#         ['U62','R66','U55','R34','D71','R55','D58','R83']]
#
# path = [['R8','U5','L5','D3'],
#         ['U7','R6','D4','L4']]

# PART 1
coors = [[], []]

for ip in range(len(path)):
    cur_x = 0
    cur_y = 0
    for p in path[ip]:
        direction = p[0]
        step = p.replace(direction, '')
        for i in range(0, int(step)):
            if direction == 'U':
                cur_y += 1
            elif direction == 'D':
                cur_y -= 1
            elif direction == 'R':
                cur_x += 1
            elif direction == 'L':
                cur_x -= 1
            coors[ip].append((cur_x, cur_y))

cross = set(coors[0]) & set(coors[1])
# print(cor_first)
# print(cor_second)
# print(cross)
min_dis = 10000000
for c in cross:
    if abs(c[0]) + abs(c[1]) < min_dis:
        min_dis = abs(c[0]) + abs(c[1])

print(min_dis)

# PART 2
cross = list(cross)
path_to_cross = [0] * len(cross)
path1 = 0
path2 = 0
for c in coors[0]:
    path1 += 1
    if c in cross:
        path_to_cross[cross.index(c)] = path1

for c in coors[1]:
    path2 += 1
    if c in cross:
        path_to_cross[cross.index(c)] += path2

print(min(path_to_cross))
