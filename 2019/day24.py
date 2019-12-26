import copy


data = '''....#
#..#.
#..##
..#..
#....'''
data = open('input/day24.txt').read()


def decode(map):
    return ''.join([''.join(a[1:-1]) for a in map][1:-1])


def print_map(map):
    print('\n'.join([''.join(a[1:-1]) for a in map][1:-1]) + '\n')


def print_map_adv(map):
    print('\n' + '-'*10)
    sub1 = map[3][3][:5]
    sub2 = map[3][3][15] + '   ' + map[3][3][5]
    sub3 = map[3][3][14] + '   ' + map[3][3][6]
    sub4 = map[3][3][13] + '   ' + map[3][3][7]
    sub5 = ''.join(reversed(map[3][3][8:13]))

    for i in range(len(map)):
        for j in range(len(map[i])):
            if i == 3 and j == 2:
                print(map[i][j], end='')
            elif i == 3 and j == 3:
                print('  ' + sub3 + '  ', end='')
            else:
                print(map[i][j] + '    ', end='')
        if i == 2:
            print('\n' + ' '*13 + sub1)
            print(' '*13 + sub2)
        elif i == 3:
            print('\n' + ' '*13 + sub4)
            print(' '*13 + sub5)
        elif i < 6:
            print('\n\n\n', end='')


def get_zero_map():
    return [['0'] * 7 for _ in range(7)]


def get_zero_map_adv():
    m = [['0'] * 7 for _ in range(7)]
    m[3][3] = '0'*16
    return m


def get_center_value(upper_layer):
    return ''.join([upper_layer[1][1], upper_layer[1][2], upper_layer[1][3], upper_layer[1][4],
                    upper_layer[1][5], upper_layer[2][5], upper_layer[3][5], upper_layer[4][5],
                    upper_layer[5][5], upper_layer[5][4], upper_layer[5][3], upper_layer[5][2],
                    upper_layer[5][1], upper_layer[4][1], upper_layer[3][1], upper_layer[2][1]])


def get_border_value(layer, lower_layer):
    layer[0][1] = layer[0][2] = layer[0][3] = layer[0][4] = layer[0][5] = lower_layer[2][3]
    layer[1][6] = layer[2][6] = layer[3][6] = layer[4][6] = layer[5][6] = lower_layer[3][4]
    layer[6][1] = layer[6][2] = layer[6][3] = layer[6][4] = layer[6][5] = lower_layer[4][3]
    layer[1][0] = layer[2][0] = layer[3][0] = layer[4][0] = layer[5][0] = lower_layer[3][2]

    return layer


# PART 1
bug_map = []
data = data.replace('.', '0').replace('#', '1')
bug_map.append(['0']*7)
for line in data.split('\n'):
    bug_map.append(['0'] + list(line) + ['0'])
bug_map.append(['0']*7)

# print_map(bug_map)

state_list = []
cs = copy.copy(bug_map)
ns = get_zero_map()
while True:
    for i in range(1, 6):
        for j in range(1, 6):
            if cs[i][j] == '1':
                if int(cs[i - 1][j]) + int(cs[i + 1][j]) + int(cs[i][j - 1]) + int(cs[i][j + 1]) == 1:
                    ns[i][j] = '1'
                else:
                    ns[i][j] = '0'
            else:
                if 1 <= int(cs[i - 1][j]) + int(cs[i + 1][j]) + int(cs[i][j - 1]) + int(cs[i][j + 1]) <= 2:
                    ns[i][j] = '1'

    state = decode(ns)
    if state not in state_list:
        state_list.append(state)
        cs = copy.deepcopy(ns)
    else:
        # print_map(ns)
        break

biodiversity_rating = 0
for i in range(len(state)):
    if state[i] == '1':
        biodiversity_rating += pow(2, i)
print('Biodiversity rating:', biodiversity_rating)

# PART 2
bug_map[3][3] = '0'*16

layer_bef = get_zero_map_adv()
layer_bef[3][3] = get_center_value(bug_map)
layer_aft = get_zero_map_adv()
layer_aft = get_border_value(layer_aft, bug_map)

layers = [layer_bef, copy.deepcopy(bug_map), layer_aft]

minute = 0
min_count = 200
while True:
    minute += 1

    # Calculate next state
    for layer in layers:
        cs = copy.deepcopy(layer)
        ns = copy.deepcopy(layer)
        # print_map_adv(cs)

        for i in range(1, 6):
            for j in range(1, 6):
                if i == 3 and j == 3:
                    continue
                n = int(cs[i - 1][j]) if len(cs[i - 1][j]) <= 1 else sum(map(int, list(cs[i - 1][j][8:13])))
                s = int(cs[i + 1][j]) if len(cs[i + 1][j]) <= 1 else sum(map(int, list(cs[i + 1][j][0:5])))
                w = int(cs[i][j - 1]) if len(cs[i][j - 1]) <= 1 else sum(map(int, list(cs[i][j - 1][4:9])))
                e = int(cs[i][j + 1]) if len(cs[i][j + 1]) <= 1 else sum(map(int, list(cs[i][j + 1][12:16]) + [cs[i][j + 1][0]]))

                if cs[i][j] == '1':
                    if n + s + w + e == 1:
                        ns[i][j] = '1'
                    else:
                        ns[i][j] = '0'
                else:
                    if 1 <= n + s + w + e <= 2:
                        ns[i][j] = '1'

        layers[layers.index(layer)] = copy.deepcopy(ns)
        # print_map_adv(layer)

    # Update state of inner and outer value
    for i in range(len(layers)):
        if i < len(layers) - 1:
            layers[i][3][3] = get_center_value(layers[i + 1])
        if i > 0:
            layers[i] = get_border_value(layers[i], layers[i-1])

    # Extend layers if needed
    outer = sum(map(int,
                    layers[0][1][1:6] +
                    [r[5] for r in layers[0]][1:6] +
                    layers[0][5][1:6] +
                    [r[1] for r in layers[0]][1:6]
                    ))
    if outer > 0:
        layer = get_zero_map_adv()
        layer[3][3] = get_center_value(layers[0])
        layers.insert(0, layer)

    inner = int(layers[len(layers)-1][2][3]) + int(layers[len(layers)-1][3][4]) + \
        int(layers[len(layers) - 1][4][3]) + int(layers[len(layers)-1][3][2])

    if inner > 0:
        layer = get_zero_map_adv()
        layer = get_border_value(layer, layers[len(layers)-1])
        layers.append(layer)

    for layer in layers:
        cs = copy.deepcopy(layer)
        ns = copy.deepcopy(layer)
        # print_map_adv(cs)

    if minute >= min_count:
        bug_count = 0
        for layer in layers:
            bug_count += sum(map(int, layer[1][1:6] + layer[2][1:6] + layer[4][1:6] + layer[5][1:6]))
            bug_count += sum(map(int, layer[3][1:3] + layer[3][4:6]))
        print('Bug count:', bug_count)
        break
