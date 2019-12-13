ins = list(map(int, open('input/day05.txt').read().split(',')))
input = 1  # part 1 input
input = 5  # part 2 input

# PART 1 + PART 2 can be merged
index = 0
while True:
    if ins[index] == 3:
        ins[ins[index+1]] = input
        index += 2
    elif ins[index] == 4:
        print('Output:', ins[ins[index+1]])
        index += 2
    elif ins[index] == 104:
        print('Output:', ins[index+1])
        index += 2
    elif ins[index] == 99:
        break
    else:
        param_mode = [0, 0]
        opcode = ''.join(reversed(str(ins[index])))
        if len(opcode) >= 3 and opcode[2] == '1':
            param_mode[0] = 1
        if len(opcode) >= 4 and opcode[3] == '1':
            param_mode[1] = 1

        value_1 = ins[ins[index+1]] if param_mode[0] == 0 else ins[index+1]
        value_2 = ins[ins[index+2]] if param_mode[1] == 0 else ins[index+2]

        if ins[index] % 10 == 1:
            ins[ins[index + 3]] = value_1 + value_2
            index += 4
        elif ins[index] % 10 == 2:
            ins[ins[index + 3]] = value_1 * value_2
            index += 4
        elif ins[index] % 10 == 5:
            if value_1 != 0:
                index = value_2
            else:
                index += 3
        elif ins[index] % 10 == 6:
            if value_1 == 0:
                index = value_2
            else:
                index += 3
        elif ins[index] % 10 == 7:
            ins[ins[index + 3]] = 1 if value_1 < value_2 else 0
            index += 4
        elif ins[index] % 10 == 8:
            ins[ins[index + 3]] = 1 if value_1 == value_2 else 0
            index += 4
