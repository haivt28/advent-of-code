input = open('input/day07.txt').read()


def count_able_to_contain_bag(bag, my_bag):
    global total
    child = parent_dict[bag]
    if len(child) > 0:
        for cb in child:
            if cb[1] == my_bag:
                total += 1
            else:
                count_able_to_contain_bag(cb[1], my_bag)


def count_required_bag(bag, multiplier):
    global count
    child = parent_dict[bag]
    if len(child) > 0:
        for cb in child:
            count += multiplier * int(cb[0])
            count_required_bag(cb[1], multiplier * int(cb[0]))


parent_dict = {}
for line in input.split('\n'):
    parent_bag = line.split('contain')[0].replace('bags', '').replace('bag', '').strip()
    child_bags = line.split('contain')[1].replace('bags', '').replace('bag', '').replace('.', '')\
        .strip().split(', ')
    norm_child_bags = []
    for b in child_bags:
        if b == 'no other':
            continue
        norm_child_bags.append((b.split()[0], b.replace(b.split()[0], '').strip()))

    parent_dict[parent_bag] = norm_child_bags


# PART 1
count = 0
MY_BAG = 'shiny gold'
for k in parent_dict:
    total = 0
    count_able_to_contain_bag(k, MY_BAG)
    if total > 0:
        count += 1
print(count)


# PART 2
count = 0
count_required_bag(MY_BAG, 1)
print(count)
