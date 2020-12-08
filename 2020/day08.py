import copy


def execute(instructions):
    value = 0
    index = 0
    traveled_ins = [False] * len(instructions)

    while True:
        # Normal instruction
        if index >= len(instructions):
            return True, value

        # Corrupted instruction with infinity loop
        if traveled_ins[index]:
            return False, value

        # Execute instructions
        traveled_ins[index] = True
        ins, arg = instructions[index]
        if ins == 'nop':
            index += 1

        elif ins == 'acc':
            value += int(arg)
            index += 1

        elif ins == 'jmp':
            index += int(arg)


if __name__ == '__main__':
    input = open('input/day08.txt').read()

    # PART 1
    ins = []
    for line in input.split('\n'):
        ins.append((line.split(' ')[0], line.split(' ')[1]))

    _, val = execute(ins)
    print(val)

    # PART 2
    for i in range(len(ins)):
        cp_ins = copy.deepcopy(ins)
        if ins[i][0] == 'nop':
            cp_ins[i] = ('jmp', ins[i][1])
        elif ins[i][0] == 'jmp':
            cp_ins[i] = ('nop', ins[i][1])

        valid_ins, val = execute(cp_ins)
        if valid_ins:
            print(val)
            break
