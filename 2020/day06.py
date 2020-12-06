input = open('input/day06.txt').read()


# PART 1
count = 0
answer_set = set()
for line in (input+'\n').split('\n'):
    if line == '':
        count += len(answer_set)
        answer_set.clear()
    else:
        for ans in line:
            answer_set.add(ans)

print(count)


# PART 2
count = 0
answer_map = {}
people_count = 0
for line in (input+'\n').split('\n'):
    if line == '':
        for k in answer_map:
            if answer_map[k] == people_count:
                count += 1
        answer_map = {}
        people_count = 0
    else:
        people_count += 1
        for ans in line:
            answer_map[ans] = 1 if ans not in answer_map else answer_map[ans] + 1

print(count)
