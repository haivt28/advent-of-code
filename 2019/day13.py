from day09 import intcode_computer
import os
import time


def update_playground(ip_output):
    global all_output, output_ins, output_id, init_game_yet, playground, width, height, score

    output_ins[output_id] = ip_output
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
            print_pg(all_output, playground, score)
            return 1 if paddle[0] < ball[0] else -1

    return None


def halt_playground():
    playground = init_playground(width, height)  # for Part 1
    print_pg(all_output, playground, score)


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

# PART 1 + PART 2 can be merged
ins[0] = 1  # Part 1 input
ins[0] = 2  # Part 2 input
input = 0   # Joystick position: 0: Neutral | 1: Tilt right | -1: Tilt left

all_output = []
output_ins = [0, 0, 0]
output_id = 0

init_game_yet = False
playground = None
width = 0
height = 0
score = 0

intcode_computer(ins, input, update_playground, halt_playground)
