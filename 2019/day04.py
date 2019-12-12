import math


count = 0
for i in range(130254, 678275):
    i0 = i % 10
    i1 = math.floor(i/10) % 10
    i2 = math.floor(i/100) % 10
    i3 = math.floor(i/1000) % 10
    i4 = math.floor(i/10000) % 10
    i5 = math.floor(i/100000) % 10
    if i0 == i1 or i1 == i2 or i2 == i3 or i3 == i4 or i4 == i5:
        if i0 >= i1 >= i2 >= i3 >= i4 >= i5:
            if i0 == i1 != i2 or i0 != i1 == i2 != i3 or i1 != i2 == i3 != i4 or i2 != i3 == i4 != i5 or i3 != i4 == i5:
                count += 1

print(count)
