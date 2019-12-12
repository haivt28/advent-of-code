import copy


ins0 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,6,23,27,1,6,27,31,2,31,9,35,1,35,6,39,1,10,39,43,2,9,43,47,1,5,47,51,2,51,6,55,1,5,55,59,2,13,59,63,1,63,5,67,2,67,13,71,1,71,9,75,1,75,6,79,2,79,6,83,1,83,5,87,2,87,9,91,2,9,91,95,1,5,95,99,2,99,13,103,1,103,5,107,1,2,107,111,1,111,5,0,99,2,14,0,0]
output = 19690720

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
