ins = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
ins = list(map(int, open('input/day09.txt').read().split(',')))


# Output of this day will be a complete Intcode computer!
def intcode_computer(ins, input, update_input_func, halt_func=None):
    buffer_size = 1000
    ins_buffer = [0] * buffer_size
    ins = ins_buffer + ins + ins_buffer

    index = buffer_size
    rbase = 0

    input_list = None
    input_id = 1
    if isinstance(input, list):
        input_list = input
        input = input_list[0]

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
            index += 2
            new_input = update_input_func(ins[param_1])
            if new_input is not None:
                if new_input == 'HALT':
                    return
                input = new_input
            if input_list is not None:
                if input_id >= len(input_list):
                    return
                else:
                    input = input_list[input_id]
                    input_id += 1
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
            if halt_func is not None:
                halt_func()
            break
        # print(ins)


def print_output(output):
    print('Output:', output)
    return 0


if __name__ == "__main__":
    # PART 1 + PART 2 can be merged
    input = 1  # Part 1 input
    input = 2  # Part 2 input

    intcode_computer(ins, input, print_output)