import copy


ins0 = list(map(int, open('input/day02.txt').read().split(',')))
output = 19690720

# PART 1 + PART 2 can be merged
for i in range(100):
    for j in range(100):
        ins = copy.copy(ins0)
        ins[1] = i
        ins[2] = j
        index = 0
        while True:
            if ins[index] == 99:
                if i == 12 and j == 2:
                    print(ins[0])
                if ins[0] == output:
                    print(i, j)
                break
            else:
                value_1 = ins[ins[index + 1]]
                value_2 = ins[ins[index + 2]]

                if ins[index] % 10 == 1:
                    ins[ins[index + 3]] = value_1 + value_2
                    index += 4
                elif ins[index] % 10 == 2:
                    ins[ins[index + 3]] = value_1 * value_2
                    index += 4
