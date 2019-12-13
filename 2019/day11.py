ins = list(map(int, open('input/day11.txt').read().split(',')))

# PART 1 + PART 2 can be merged
input = 0  # Part 1 input
input = 1  # Part 2 input

buffer_size = 1000
ins_buffer = [0] * buffer_size
ins = ins_buffer + ins + ins_buffer

index = buffer_size
rbase = 0

panels = {}
current_pos = [0, 0]  # robot coordinate
current_dir = 1  # 1-North | 2-East | 3-South | 4-West
output = [0, 0, 0]  # color, direction, output_index

min_x = 10000000
max_x = -10000000
min_y = 10000000
max_y = -10000000

while True:
    # INSTRUCTION FORMAT: ABCDE, Param1, [Param2, Param3]
    #   DE: two-digit opcode
    #    C: mode of 1st parameter
    #    B: mode of 2nd parameter
    #    A: mode of 3rd parameter
    # PARAMETER MODES:
    #    0: Position mode
    #    1: Immediate mode
    #    2: Relative mode
    param_mode = [0, 0, 0]

    # Calculate parameters mode
    ins_string = ''.join(reversed(str(ins[index])))
    if len(ins_string) >= 3:
        param_mode[0] = int(ins_string[2])
    if len(ins_string) >= 4:
        param_mode[1] = int(ins_string[3])
    if len(ins_string) >= 5:
        param_mode[2] = int(ins_string[4])

    # Calculate parameters index value
    if param_mode[0] == 1:
        param_1 = index + 1
    elif param_mode[0] == 2:
        param_1 = ins[index + 1] + rbase + buffer_size
    else:
        param_1 = ins[index + 1] + buffer_size
    if param_mode[1] == 1:
        param_2 = index + 2
    elif param_mode[1] == 2:
        param_2 = ins[index + 2] + rbase + buffer_size
    else:
        param_2 = ins[index + 2] + buffer_size
    if param_mode[2] == 2:
        param_3 = ins[index + 3] + rbase + buffer_size
    else:
        param_3 = ins[index + 3] + buffer_size

    # Execute based on opcode
    opcode = ins[index] % 100
    # print('opcode', opcode, ins[index])
    if opcode == 3:  # INPUT
        ins[param_1] = input
        index += 2
    elif opcode == 4:  # OUTPUT
        # print('Output:', ins[param_1])
        index += 2

        output[output[2]] = ins[param_1]
        output[2] = 1 if output[2] == 0 else 0

        if output[2] == 0:
            if min_x > current_pos[0]: min_x = current_pos[0]
            if max_x < current_pos[0]: max_x = current_pos[0]
            if min_y > current_pos[1]: min_y = current_pos[1]
            if max_y < current_pos[1]: max_y = current_pos[1]

            panels[tuple(current_pos)] = output[0]
            print('-' * 10)
            print('Paint:', 'Black' if output[0] == 0 else 'White')
            print('Turn:', 'Right' if output[1] == 1 else 'Left')
            print('Panels:', current_pos + [output[0]])
            print('before_dir:', current_dir)
            current_dir = current_dir + 1 if output[1] == 1 else current_dir - 1
            if current_dir > 4:
                current_dir = 1
            if current_dir < 1:
                current_dir = 4
            print('current_dir:', current_dir)
            print(current_pos)

            if current_dir == 1:
                current_pos[1] += 1
            elif current_dir == 2:
                current_pos[0] += 1
            elif current_dir == 3:
                current_pos[1] -= 1
            elif current_dir == 4:
                current_pos[0] -= 1

            input = panels[tuple(current_pos)] if tuple(current_pos) in panels else 0

    elif opcode == 9:  # ADJUST RELATIVE BASE
        rbase += ins[param_1]
        # print('R-base:', rbase)
        index += 2
    elif opcode == 1:  # ADD
        ins[param_3] = ins[param_1] + ins[param_2]
        index += 4
    elif opcode == 2:  # MULTIPLY
        ins[param_3] = ins[param_1] * ins[param_2]
        index += 4
    elif opcode == 5:  # JUMP IF TRUE
        if ins[param_1] != 0:
            index = ins[param_2] + buffer_size
        else:
            index += 3
    elif opcode == 6:  # JUMP IF FALSE
        if ins[param_1] == 0:
            index = ins[param_2] + buffer_size
        else:
            index += 3
    elif opcode == 7:  # LESS THAN
        ins[param_3] = 1 if ins[param_1] < ins[param_2] else 0
        index += 4
    elif opcode == 8:  # EQUALS
        ins[param_3] = 1 if ins[param_1] == ins[param_2] else 0
        index += 4
    elif opcode == 99:  # HALT!
        break
    # print(ins)

print(len(panels))
print(min_x, min_y, max_x, max_y)

out = [[0 for j in range(abs(min_x) + max_x + 1)] for i in range(abs(min_y) + max_y + 1)]
for key in panels:
    if panels[key] == 1:
        out[abs(min_y) + key[1]][abs(min_x) + key[0]] = 1

for i in reversed(range(len(out))):
    print(''.join(str(x) for x in out[i]).replace('1', '#').replace('0', ' '))
