import copy


def play_game(p1, p2, recursive_combat=False):
    state_p1 = []
    state_p2 = []

    while len(p1) > 0 and len(p2) > 0:
        if ''.join(map(str, p1)) in state_p1 and ''.join(map(str, p2)) in state_p2:
            return p1, []

        state_p1.append(''.join(map(str, p1)))
        state_p2.append(''.join(map(str, p2)))

        p1_play = p1.pop(0)
        p2_play = p2.pop(0)

        sub_p1 = sub_p2 = None
        if recursive_combat and len(p1) >= p1_play and len(p2) >= p2_play:
            sub_p1, sub_p2 = play_game(p1[:p1_play], p2[:p2_play], recursive_combat)

        if sub_p1 is not None and sub_p2 is not None and len(sub_p1) > 0:
            p1.extend([p1_play, p2_play])
        elif sub_p1 is not None and sub_p2 is not None and len(sub_p2) > 0:
            p2.extend([p2_play, p1_play])
        elif p1_play > p2_play:
            p1.extend([p1_play, p2_play])
        else:
            p2.extend([p2_play, p1_play])

    return p1, p2


def calculate_winner(p1, p2):
    res = 0
    if len(p1) > 0:
        index = 1
        for i in reversed(range(len(p1))):
            res += p1[i] * index
            index += 1
    else:
        index = 1
        for i in reversed(range(len(p2))):
            res += p2[i] * index
            index += 1

    return res


input = open('input/day22.txt').read()

player1 = []
player2 = []
current_player = None
for line in input.split('\n'):
    if 'Player 1' in line:
        current_player = 1
    elif 'Player 2' in line:
        current_player = 2

    if current_player == 1 and 'Player' not in line and line != '':
        player1.append(int(line))
    elif current_player == 2 and 'Player' not in line and line != '':
        player2.append(int(line))


# PART 1
p1, p2 = play_game(copy.deepcopy(player1), copy.deepcopy(player2))
print(calculate_winner(p1, p2))

# PART 2
p1, p2 = play_game(copy.deepcopy(player1), copy.deepcopy(player2), recursive_combat=True)
print(calculate_winner(p1, p2))
