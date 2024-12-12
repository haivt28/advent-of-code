report = list(map(str, open('input/day11.txt').read().split(' ')))

stone_cache = {}
for s in report:
    stone_cache[s] = 1

def check_stone(stone, n_stone):
    if stone not in stone_cache:
        stone_cache[stone] = 0
    stone_cache[stone] += n_stone

def process(stone, n_stone):
    stone_cache[stone] -= n_stone

    if stone == '0':
        check_stone('1', n_stone)
    elif len(stone) % 2 == 0:
        l = int(len(stone) / 2)
        left_stone = stone[:l]
        right_stone = stone[l:].lstrip('0')
        if right_stone == '':
            right_stone = '0'

        check_stone(left_stone, n_stone)
        check_stone(right_stone, n_stone)
    else:
        new_stone = int(stone) * 2024
        check_stone(str(new_stone), n_stone)

def blink():
    stones = {k: v for k, v in stone_cache.items() if v > 0}
    for key, value in stones.items():
        process(key, value)

for turn in range(75):
    blink()

    # PART 1
    if turn == 24:
        print(sum(stone_cache.values()))

# PART 2
print(sum(stone_cache.values()))