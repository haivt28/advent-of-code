input = list(map(int, open('input/day15.txt').read().split(',')))

last_spoken = input.pop()
spoken = {}
turn = 1
for i in input:
    spoken[i] = [turn, turn]
    turn += 1

while True:
    turn += 1

    if last_spoken not in spoken:
        spoken[last_spoken] = [turn - 1, turn - 1]

    last_spoken = spoken[last_spoken][0] - spoken[last_spoken][1]

    if last_spoken in spoken:
        spoken[last_spoken].pop()
        spoken[last_spoken].insert(0, turn)

    # PART 1
    if turn == 2020:
        print(last_spoken)

    # PART 2
    if turn == 30000000:
        print(last_spoken)
        break
