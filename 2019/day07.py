import copy
import itertools


ins = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 42, 67, 88, 101, 114, 195, 276, 357, 438, 99999, 3, 9, 101, 3, 9, 9,
       1002, 9, 4, 9, 1001, 9, 5, 9, 102, 4, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 3, 9, 1002, 9, 2, 9, 101, 2, 9, 9, 102, 2,
       9, 9, 1001, 9, 5, 9, 4, 9, 99, 3, 9, 102, 4, 9, 9, 1001, 9, 3, 9, 102, 4, 9, 9, 101, 4, 9, 9, 4, 9, 99, 3, 9,
       101, 2, 9, 9, 1002, 9, 3, 9, 4, 9, 99, 3, 9, 101, 4, 9, 9, 1002, 9, 5, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3,
       9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9,
       1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002,
       9, 2, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9,
       2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9,
       4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4,
       9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3,
       9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 99, 3, 9,
       102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 1,
       9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9,
       4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 99, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4,
       9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3,
       9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99]

# ins = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
sequence = [copy.copy(ins)] * 5

# phase_sequence = [0,1,2,3,4]
phase = [9, 7, 8, 5, 6]
permute_ps = list(itertools.permutations(phase))
max_output = 0

for pps in permute_ps:
    input = 0
    index = [0] * 5

    index_sequence = 0
    is_first_loop = True
    while True:
        is_first_input = True and is_first_loop
        # index = 0
        ins = sequence[index_sequence]
        is_break = False
        while True:
            cindex = index[index_sequence]
            if ins[cindex] == 3:
                ins[ins[cindex + 1]] = pps[index_sequence] if is_first_input else input
                is_first_input = False
                index[index_sequence] += 2
            elif ins[cindex] == 4:
                input = ins[ins[cindex + 1]]
                if max_output < input:
                    max_output = input
                index[index_sequence] += 2
                break
            elif ins[cindex] == 104:
                input = ins[cindex + 1]
                if max_output < input:
                    max_output = input
                index[index_sequence] += 2
                break
            elif ins[cindex] == 99:
                # print(ins)
                # print('HALT!')
                is_break = True
                break
            else:
                param_mode = [0, 0]
                opcode = ''.join(reversed(str(ins[cindex])))
                if len(opcode) >= 3 and opcode[2] == '1':
                    param_mode[0] = 1
                if len(opcode) >= 4 and opcode[3] == '1':
                    param_mode[1] = 1

                value_1 = ins[ins[cindex + 1]] if param_mode[0] == 0 else ins[cindex + 1]
                value_2 = ins[ins[cindex + 2]] if param_mode[1] == 0 else ins[cindex + 2]

                if ins[cindex] % 10 == 1:
                    ins[ins[cindex + 3]] = value_1 + value_2
                    index[index_sequence] += 4
                elif ins[cindex] % 10 == 2:
                    ins[ins[cindex + 3]] = value_1 * value_2
                    index[index_sequence] += 4
                elif ins[cindex] % 10 == 5:
                    if value_1 != 0:
                        index[index_sequence] = value_2
                    else:
                        index[index_sequence] += 3
                elif ins[cindex] % 10 == 6:
                    if value_1 == 0:
                        index[index_sequence] = value_2
                    else:
                        index[index_sequence] += 3
                elif ins[cindex] % 10 == 7:
                    ins[ins[cindex + 3]] = 1 if value_1 < value_2 else 0
                    index[index_sequence] += 4
                elif ins[cindex] % 10 == 8:
                    ins[ins[cindex + 3]] = 1 if value_1 == value_2 else 0
                    index[index_sequence] += 4

        sequence[index_sequence] = ins

        index_sequence += 1
        if index_sequence > 4:
            index_sequence = 0
            is_first_loop = False
        if is_break and index_sequence == 0:
            break

print(max_output)
