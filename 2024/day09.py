report = list(open('input/day09.txt').read())

blocks = []
files = {}

id_number = 0
for id in range(len(report)):
    if id % 2 == 0:
        blocks.extend([str(id_number)] * int(report[id]))
        files[str(id_number)] = int(report[id])
        id_number += 1
    else:
        blocks.extend(['.'] * int(report[id]))


def checksum(blocks):
    sum = 0
    for id in range(len(blocks)):
        if blocks[id] == '.':
            continue
        else:
            sum += id * int(blocks[id])
    return sum

# PART 1
last_index = len(blocks)
optimized_blocks = blocks.copy()

for idx in range(len(blocks)):
    if blocks[idx] == '.':
        for idy in reversed(range(last_index)):
            if idy < idx:
                break

            if blocks[idy] != '.':
                optimized_blocks[idx] = blocks[idy]
                optimized_blocks[idy] = '.'
                last_index = idy
                break

print(checksum(optimized_blocks))


# PART 2
checked_files = []

for idy in reversed(range(len(blocks))):
    if blocks[idy] not in checked_files and blocks[idy] != '.':
        checked_files.append(blocks[idy])

        free_space_count = 0
        free_space_index = 0
        for idx in range(len(blocks)):
            if blocks[idx] == '.':
                if free_space_count == 0:
                    free_space_index = idx
                free_space_count += 1
            else:
                free_space_count = 0

            if free_space_count >= files[blocks[idy]] and free_space_index < idy - files[blocks[idy]]:
                blocks[free_space_index:free_space_index+free_space_count] = [blocks[idy]] * files[blocks[idy]]
                blocks[idy - files[blocks[idy]]+1:idy+1] = ['.'] * files[blocks[idy]]
                break

print(checksum(blocks))