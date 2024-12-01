report = list(map(int, open('input/day01.txt').read().split()))

# PART 1
loc1 = sorted(report[::2])
loc2 = sorted(report[1::2])

total_distance = 0
for id, x in enumerate(loc1):
    total_distance += abs(loc1[id] - loc2[id])

print(total_distance)


# PART 2
similarity = 0
for id, x in enumerate(loc1):
    similarity += loc1[id] * loc2.count(loc1[id])

print(similarity)
