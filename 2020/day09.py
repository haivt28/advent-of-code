import itertools


input = open('input/day09.txt').read()


# PART 1
size = 25
preamble = list(map(int, input.split('\n')))
invalid = 0

for i in range(size, len(preamble)):
    valid = False
    for pair in list(itertools.combinations(preamble[i-size:i], 2)):
        if pair[0] + pair[1] == preamble[i]:
            valid = True
            break
    if not valid:
        invalid = preamble[i]
        break

print(invalid)


# PART 2
window_size = 2
weakness = None
previous_pre = preamble[0:i]
while not weakness:
    for i in range(0, len(previous_pre) - window_size + 1):
        window = previous_pre[i:i+window_size]
        if sum(window) == invalid:
            weakness = min(window) + max(window)
            break
    window_size += 1

print(weakness)
