from day09 import intcode_computer


def update_panel(ip_output):
    global min_x, max_x, min_y, max_y, panels, current_pos, current_dir, output

    output[output[2]] = ip_output
    output[2] = 1 if output[2] == 0 else 0

    if output[2] == 0:
        if min_x > current_pos[0]: min_x = current_pos[0]
        if max_x < current_pos[0]: max_x = current_pos[0]
        if min_y > current_pos[1]: min_y = current_pos[1]
        if max_y < current_pos[1]: max_y = current_pos[1]

        panels[tuple(current_pos)] = output[0]
        # print('-' * 10)
        # print('Paint:', 'Black' if output[0] == 0 else 'White')
        # print('Turn:', 'Right' if output[1] == 1 else 'Left')
        # print('Panels:', current_pos + [output[0]])
        # print('before_dir:', current_dir)
        current_dir = current_dir + 1 if output[1] == 1 else current_dir - 1
        if current_dir > 4:
            current_dir = 1
        if current_dir < 1:
            current_dir = 4
        # print('current_dir:', current_dir)
        # print(current_pos)

        if current_dir == 1:
            current_pos[1] += 1
        elif current_dir == 2:
            current_pos[0] += 1
        elif current_dir == 3:
            current_pos[1] -= 1
        elif current_dir == 4:
            current_pos[0] -= 1

        return panels[tuple(current_pos)] if tuple(current_pos) in panels else 0


ins = list(map(int, open('input/day11.txt').read().split(',')))

# PART 1 + PART 2 can be merged
input = 0  # Part 1 input
input = 1  # Part 2 input

panels = {}
current_pos = [0, 0]  # robot coordinate
current_dir = 1  # 1-North | 2-East | 3-South | 4-West
output = [0, 0, 0]  # color, direction, output_index

min_x = 10000000
max_x = -10000000
min_y = 10000000
max_y = -10000000

intcode_computer(ins, input, update_panel)

print(len(panels))
# print(min_x, min_y, max_x, max_y)

out = [[0 for j in range(abs(min_x) + max_x + 1)] for i in range(abs(min_y) + max_y + 1)]
for key in panels:
    if panels[key] == 1:
        out[abs(min_y) + key[1]][abs(min_x) + key[0]] = 1

for i in reversed(range(len(out))):
    print(''.join(str(x) for x in out[i]).replace('1', '#').replace('0', ' '))
