input = open('input/day10.txt').read()


# PART 1
adapters = list(map(int, input.split('\n')))
adapters = sorted(adapters)

init = 0
count1 = 0
count3 = 0
for adapt in adapters:
    if adapt - init == 1:
        count1 += 1
    if adapt - init == 3:
        count3 += 1
    init = adapt

print(count1*(count3+1))


# PART 2
# Solution 1: Find set of pattern
#   Split adapters into groups of consecutive ones,
#   then calculate the possibility of each group and multiply them.
#   For example:
#       - Group of 3 consecutive adapters has 2 cases
#       - Group of 4 consecutive adapters has 4 cases
#       - Group of 5 consecutive adapters has 7 cases
adapters = [0] + adapters + [max(adapters) + 3]
count = 1
res = 1
for i in range(1, len(adapters)):
    if adapters[i] == adapters[i - 1] + 1:
        count += 1
    else:
        if count == 5:
            res *= 7
        elif count == 4:
            res *= 4
        elif count == 3:
            res *= 2
        count = 1

print(res)


# Solution 2: Dynamic Programming (Top Down)
traveled_cost = {}


def travel(adapter):
    global traveled_cost
    if adapter not in adapters:
        return 0

    if adapter not in traveled_cost:
        traveled_cost[adapter] = travel(adapter - 1) + travel(adapter - 2) + travel(adapter - 3)

    return traveled_cost[adapter]


travel(max(adapters))
print(res)


# Solution 3: Dynamic Programming (Bottom Up)
adapters = [100, 100] + adapters
cost = {100: 0, 0: 1}
for i in range(3, len(adapters)):
    current_adapter = adapters[i]
    current_cost = 0

    if current_adapter - adapters[i-1] <= 3:
        current_cost += cost[adapters[i-1]]

    if current_adapter - adapters[i-2] <= 3:
        current_cost += cost[adapters[i-2]]

    if current_adapter - adapters[i-3] <= 3:
        current_cost += cost[adapters[i-3]]

    cost[current_adapter] = current_cost

print(cost[max(adapters)])
