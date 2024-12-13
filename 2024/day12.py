import re

report = list(map(str, open('input/day12.txt').read().split('\n')))

garden = [['#'] * (len(report[0]) + 2)]
for line in report:
    level = list(line)
    garden.append(['#'] + level + ['#'])
garden.append(['#'] * (len(report[0]) + 2))


def spread(plant, pos, area_peri, checked):
    checked.append(pos)
    area_peri[0] += 1
    directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

    area_peri[2].append(pos)

    for d in directions:
        next = [pos[0] + d[0], pos[1] + d[1]]
        if garden[next[0]][next[1]] == plant and next not in checked:
            spread(plant, next, area_peri, checked)
        elif garden[next[0]][next[1]] != plant:
            area_peri[1] += 1


def calculate_side(side):
    side = side.strip('0')
    side = re.sub(r"0+", "0", side)
    if side == '':
        return 0
    side = side.split('0')
    return len(side)


checked = []
price = 0
discount_price = 0

for x in range(1, len(garden)-1):
    for y in range(1, len(garden[x])-1):
        if garden[x][y] != '#' and [x, y] not in checked:
            # PART 1
            area_peri = [0, 0, []]
            spread(garden[x][y], [x, y], area_peri, checked)
            price += area_peri[0] * area_peri[1]


            # PART 2
            area = area_peri[2]
            side_count = 0

            for idx in range(len(garden)):
                upperside = ''
                lowerside = ''
                for idy in range(len(garden[idx])):
                    plant = garden[idx][idy]

                    if [idx, idy] in area and plant != garden[idx-1][idy]:
                        upperside += '1'
                    else:
                        upperside += '0'

                    if [idx, idy] in area and plant != garden[idx+1][idy]:
                        lowerside += '1'
                    else:
                        lowerside += '0'
                side_count += calculate_side(upperside) + calculate_side(lowerside)

            for idy in range(len(garden[0])):
                leftside = ''
                rightside = ''
                for idx in range(len(garden)):
                    plant = garden[idx][idy]

                    if [idx, idy] in area and plant != garden[idx][idy-1]:
                        leftside += '1'
                    else:
                        leftside += '0'

                    if [idx, idy] in area and plant != garden[idx][idy+1]:
                        rightside += '1'
                    else:
                        rightside += '0'
                side_count += calculate_side(leftside) + calculate_side(rightside)

            discount_price += area_peri[0] * side_count

print(price)
print(discount_price)