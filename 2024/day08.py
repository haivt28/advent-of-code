report = list(map(str, open('input/day08.txt').read().split('\n')))

map = []
antinode_map_1 = []
antinode_map_2 = []
antennas_dict = {}


for idx in range(len(report)):
    line = list(report[idx])
    map.append(line)
    antinode_map_1.append([0] * len(line))
    antinode_map_2.append([0] * len(line))
    for idy in range(len(line)):
        signal = line[idy]
        if signal != '.':
            if signal not in antennas_dict:
                antennas_dict[signal] = []
            antennas_dict[signal].append([map.index(line), line.index(signal)])


for key, value in antennas_dict.items():
    for antenna_1 in range(len(value)):
        for antenna_2 in range(len(value)):
            if antenna_1 != antenna_2:
                range_x = value[antenna_2][0] - value[antenna_1][0]
                range_y = value[antenna_2][1] - value[antenna_1][1]

                multiplier = 1
                while True:
                    antinode_x = value[antenna_1][0] + multiplier * range_x
                    antinode_y = value[antenna_1][1] + multiplier * range_y

                    if 0 <= antinode_x < len(map) and 0 <= antinode_y < len(map[0]):
                        # PART 1
                        if multiplier == 2:
                            antinode_map_1[antinode_x][antinode_y] = 1

                        # PART 2
                        antinode_map_2[antinode_x][antinode_y] = 1
                        multiplier += 1
                    else:
                        break

print(sum(sum(antinode_map_1,[])))
print(sum(sum(antinode_map_2,[])))