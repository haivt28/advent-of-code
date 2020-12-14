input = open('input/day14.txt').read()


# PART 1
mem = {}
mask = ''
for line in input.split('\n'):
    if line.startswith('mask'):
        _, _, mask = line.split()
    else:
        location, _, value = line.split()
        location = int(location.replace('mem[', '').replace(']', ''))
        value = list('{0:036b}'.format(int(value)))
        value = [mask[i] if mask[i] != 'X' else value[i] for i in range(len(mask))]

        mem[location] = int(''.join(value), 2)

print(sum(mem.values()))


# PART 2
mem = {}
mask = ''
for line in input.split('\n'):
    if line.startswith('mask'):
        _, _, mask = line.split()
    else:
        location, _, value = line.split()
        location = int(location.replace('mem[', '').replace(']', ''))
        location = list('{0:036b}'.format(location))

        binary_index = []
        for i in range(len(mask)):
            if mask[i] != '0':
                location[i] = mask[i]
            if mask[i] == 'X':
                binary_index.append(i)

        for i in range(0, 2 ** len(binary_index)):
            binary = bin(i)[2:]
            binary = list(str(binary).zfill(len(binary_index)))

            for j in range(len(binary_index)):
                location[binary_index[j]] = binary[j]

            mem[int(''.join(location), 2)] = int(value)

print(sum(mem.values()))
