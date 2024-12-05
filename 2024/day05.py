input1 = open('input/day05.txt').read().split('\n\n')[0].split('\n')
input2 = open('input/day05.txt').read().split('\n\n')[1].split('\n')


total_part1 = 0
total_part2 = 0
rules = []

for rule in input1:
    rules.append(rule.split('|'))

for update in input2:
    update = update.split(',')
    sub_rules = []
    pages = []

    # Filter rules related to current update
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            sub_rules.append(rule)
            if rule[0] not in pages: pages.append(rule[0])
            if rule[1] not in pages: pages.append(rule[1])

    # Page index for sorting pages with related rules
    pages_index = [0] * len(pages)
    for rule in sub_rules:
        pages_index[pages.index(rule[0])] += 1

    sorted_pages = [x for _, x in sorted(zip(pages_index, pages), reverse=True)]

    # PART 1
    # If current update equals to sorted pages then it's a correctly-ordered update
    if update == sorted_pages:
        total_part1 += int(sorted_pages[int((len(sorted_pages) - 1) / 2)])

    # PART 2
    # No need to update incorrectly-ordered update, just take the sorted pages
    else:
        total_part2 += int(sorted_pages[int((len(sorted_pages) - 1) / 2)])

print(total_part1)
print(total_part2)