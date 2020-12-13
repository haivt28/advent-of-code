input = open('input/day13.txt').read()


# PART 1
my_time = int(input.split('\n')[0])
bus_list = input.split('\n')[1].split(',')

wait = []
for bus in bus_list:
    if bus != 'x':
        wait.append(my_time + int(bus) - my_time % int(bus))
    else:
        wait.append(float('inf'))

print(int(bus_list[wait.index(min(wait))]) * (min(wait) - my_time))


# PART 2
# Hint get from:
# https://www.reddit.com/r/adventofcode/comments/kc60ri/2020_day_13_can_anyone_give_me_a_hint_for_part_2/gfnnfm3/?utm_source=reddit&utm_medium=web2x&context=3
timestamp = 0
next_timestamp = 0
W = int(bus_list[0])
for i in range(1, len(bus_list)):
    if bus_list[i] != 'x':
        multiplier = 1
        while True:
            valid = True
            for j in range(1, i + 1):
                next_timestamp = timestamp + W * multiplier
                if bus_list[j] != 'x' and (next_timestamp + j) % int(bus_list[j]) != 0:
                    multiplier += 1
                    valid = False
                    break

            if valid:
                timestamp = next_timestamp
                W *= int(bus_list[i])
                break

print(timestamp)
