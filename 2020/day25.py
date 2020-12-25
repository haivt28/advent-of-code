input = open('input/day25.txt').read()

card_public_key = int(input.split('\n')[0])
room_public_key = int(input.split('\n')[1])


def find_loop_size(public_key):
    remainder = 1
    loop_size = 0
    while remainder != public_key:
        remainder = (remainder * 7) % 20201227
        loop_size += 1
    return loop_size


room_loop_size = find_loop_size(room_public_key)
print(pow(card_public_key, room_loop_size, 20201227))
