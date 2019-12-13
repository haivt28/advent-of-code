import os
import time


def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def init_playground(width, height):
    return [[0 for x in range(width + 1)] for y in range(height + 1)]


def print_pg(output, pg, score):
    time.sleep(0.05)
    clear()
    print('\nSCORE:', score)
    for o in output:
        pg[o[1]][o[0]] = o[2]
    for line in pg:
        print(''.join(str(x) for x in line)
              .replace('0', ' ')
              .replace('1', '#')
              .replace('2', 'x')
              .replace('3', '=')
              .replace('4', 'o'))


ins = list(map(int, open('input/day13.txt').read().split(',')))
ins[0] = 1  # Part 1 input
ins[0] = 2  # Part 2 input

# PART 1 + PART 2 can be merged
input = 0   # Joystick position: 0: Neutral | 1: Tilt right | -1: Tilt left

buffer_size = 1000
ins_buffer = [0] * buffer_size
ins = ins_buffer + ins + ins_buffer

index = buffer_size
rbase = 0

all_output = []
output_ins = [0, 0, 0]
output_id = 0

init_game_yet = False
playground = None
width = 0
height = 0
score = 0

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

        output_ins[output_id] = ins[param_1]
        output_id = output_id + 1 if output_id < 2 else 0
        if output_id == 0:
            if width < output_ins[0]:
                width = output_ins[0]
            if height < output_ins[1]:
                height = output_ins[1]

            if output_ins[0] == -1 and output_ins[1] == 0:
                if not init_game_yet:
                    init_game_yet = True
                    playground = init_playground(width, height)
                    print_pg(all_output, playground, 0)
                else:
                    score = output_ins[2]
            else:
                all_output.append([output_ins[0], output_ins[1], output_ins[2]])

            if output_ins[2] == 4 and init_game_yet:
                paddle = [o for o in all_output if o[2] == 3][-1]  # get last position of paddle
                ball = output_ins
                input = 1 if paddle[0] < ball[0] else -1
                print_pg(all_output, playground, score)
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
        playground = init_playground(width, height)  # for Part 1
        print_pg(all_output, playground, score)
        break
    # print(ins)
