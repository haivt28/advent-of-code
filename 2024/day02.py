report = list(map(str, open('input/day02.txt').read().split('\n')))

def check_safe(level_list):
    is_safe = True
    if level_list == sorted(level_list, reverse=False) or level_list == sorted(level_list, reverse=True):
        for id, x in enumerate(level_list):
            if abs(level_list[id] - level_list[id+1]) not in [1, 2, 3]:
                is_safe = False
                break
            if id == len(level_list) - 2:
                break
    else:
        is_safe = False

    return is_safe


# PART 1
safe_counter = 0
for line in report:
    level = list(map(int, line.split()))
    if check_safe(level):
        safe_counter += 1

print(safe_counter)


# PART 2
safe_counter = 0
for line in report:
    level = list(map(int, line.split()))
    if check_safe(level):
        safe_counter += 1
    else:
        for id, x in enumerate(level):
            tmp_level = level[:]
            tmp_level.pop(id)
            if check_safe(tmp_level):
                safe_counter += 1
                break

print(safe_counter)
