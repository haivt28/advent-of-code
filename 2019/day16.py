import numpy as np


# PART 1
# Just use some greedy calculations
input = '80871224585914546619083218645595'
input = open('input/day16.txt').read()
pattern = [0, 1, 0, -1]

input = [int(i) for i in input]

phase = 0
while True:
    new_input = []
    for index in range(len(input)):
        actual_pattern = [ele for ele in pattern for i in range(index + 1)]
        actual_pattern = list(np.resize(actual_pattern, len(input) + 1))[1:]
        digit = sum([a*b for a, b in zip(input, actual_pattern)])
        digit = abs(digit) % 10
        new_input.append(digit)

    input = new_input
    phase += 1
    if phase == 100:
        break

print(''.join(map(str, input))[0:8])


# PART 2
# Thanks to the hint about the offset:
# https://www.reddit.com/r/adventofcode/comments/ebd3o3/day_16_part_2_help/fb3vbci/
# Key points:
# 1. Number from OFFSET index doesn't related to previous number since they're all multiply with zero from pattern
# 2. Index larger than half of number's length doesn't need to care about the pattern since they are all ones
input = '03081770884921959731165446850517'
input = open('input/day16.txt').read()

offset = int(input[0:7])
repeat_input = 10000
input = [int(i) for i in input]
input = input * repeat_input
input = input[offset:]

phase = 0
while True:
    new_input = []
    sum = 0
    for index in reversed(range(len(input))):
        sum += input[index]
        new_input.append(abs(sum) % 10)

    input = list(reversed(new_input))
    phase += 1
    if phase == 100:
        break

print(''.join(map(str, input))[0:8])
