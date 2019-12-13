input = open('input/day08.txt').read()

# PART 1
layers = []
w = 25
h = 6
image = ['2'] * w * h
min_0 = 1000000000000
min_layer = ''
for i in range(1, len(input) + 1):
    if i % (w * h) == 0:
        layer = input[(i - w * h):i]
        count = layer.count('0')
        if count < min_0:
            min_0 = count
            min_layer = layer

        for j in range(0, len(image)):
            if image[j] == '2':
                image[j] = layer[j]

        # layers.append(layer)

print(min_layer.count('1') * min_layer.count('2'))

# PART 2
image = ''.join(image)
for i in range(0, h):
    print(image[i * w:i * w + w - 1].replace('1', '#').replace('0', ' '))
