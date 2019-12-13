import math


data = list(map(int, open('input/day04.txt').read().split('-')))

# PART 1 + PART 2 can be merged
count1 = 0
count2 = 0
for i in range(data[0], data[1]):
    i0 = i % 10
    i1 = math.floor(i/10) % 10
    i2 = math.floor(i/100) % 10
    i3 = math.floor(i/1000) % 10
    i4 = math.floor(i/10000) % 10
    i5 = math.floor(i/100000) % 10
    if i0 == i1 or i1 == i2 or i2 == i3 or i3 == i4 or i4 == i5:
        if i0 >= i1 >= i2 >= i3 >= i4 >= i5:
            count1 += 1
            if i0 == i1 != i2 or i0 != i1 == i2 != i3 or i1 != i2 == i3 != i4 or i2 != i3 == i4 != i5 or i3 != i4 == i5:
                count2 += 1

print(count1)
print(count2)
