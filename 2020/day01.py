import itertools

report = list(map(int, open('input/day01.txt').read().split()))


# PART 1
for pair in list(itertools.combinations(report, 2)):
    if pair[0] + pair[1] == 2020:
        print(pair[0]*pair[1])
        break

# PART 2
for triple in list(itertools.combinations(report, 3)):
    if triple[0] + triple[1] + triple[2] == 2020:
        print(triple[0]*triple[1]*triple[2])
        break
