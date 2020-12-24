def rotate(cups, n):
    return cups[n:] + cups[:n]


input = open('input/day23.txt').read()

# PART 1
cups = list(map(int, list(input)))
current_index = 0
for _ in range(100):
    current_cup = cups[current_index]
    len_pickup = 3
    if current_index+3 < len(cups):
        pick_up = cups[current_index+1:current_index+4]
    else:
        pick_up = cups[current_index+1:]
        len_pickup = len(pick_up)
        pick_up.extend(cups[:3-len(pick_up)])
    cups = [x for x in cups if (x not in pick_up)]
    destination = current_cup - 1
    while True:
        if destination in pick_up:
            destination -= 1
        elif destination != current_cup and destination >= min(cups):
            break
        elif destination < min(cups):
            destination = max(cups)

    destination_index = cups.index(destination) + 1
    cups[destination_index:destination_index] = pick_up
    if destination_index <= current_index:
        cups = rotate(cups, len_pickup)
    current_index += 1
    if current_index > len(cups) - 1:
        current_index = 0
print(''.join(map(str, rotate(cups, cups.index(1))))[1:])


# PART 2
cups = list(map(int, list(input)))

# Add more cups
for i in range(len(cups)+1, 1000000+1):
    cups.append(i)

# Use dict as a circular linked list
cups_map = {}
for i in range(len(cups)-1):
    cups_map[cups[i]] = cups[i+1]
cups_map[cups[len(cups)-1]] = cups[0]

current_cup = cups[0]
min_cup = min(cups)
max_cup = max(cups)

for _ in range(10000000):
    pickup_1st = cups_map[current_cup]
    pickup_2nd = cups_map[pickup_1st]
    pickup_3rd = cups_map[pickup_2nd]
    pickup = [pickup_1st, pickup_2nd, pickup_3rd]

    # detach pickup cups
    cups_map[current_cup] = cups_map[pickup_3rd]

    # find destination cup
    destination = current_cup - 1
    while True:
        if destination in pickup:
            destination -= 1
        elif destination != current_cup and destination >= min_cup:
            break
        elif destination < min_cup:
            destination = max_cup

    # re-attach pickup cups
    next_to_destination = cups_map[destination]
    cups_map[destination] = pickup_1st
    cups_map[pickup_3rd] = next_to_destination

    current_cup = cups_map[current_cup]

print(cups_map[1] * cups_map[cups_map[1]])
