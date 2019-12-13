import math


mass = list(map(int, open('input/day01.txt').read().split()))

# PART 1
total = 0
for m in mass:
    total += math.floor(m/3)-2

print(total)

# PART 2
total = 0
for m in mass:
    tmp = m
    while tmp > 0:
        tmp = math.floor(tmp/3)-2
        total += tmp if tmp > 0 else 0

print(total)
