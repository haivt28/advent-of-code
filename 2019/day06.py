# Testcases
input = [
    'COM)B',
    'B)C',
    'C)D',
    'D)E',
    'E)F',
    'B)G',
    'G)H',
    'D)I',
    'E)J',
    'J)K',
    'K)L'
]

input = [
    'COM)B',
    'B)C',
    'C)D',
    'D)E',
    'E)F',
    'B)G',
    'G)H',
    'D)I',
    'E)J',
    'J)K',
    'K)L',
    'K)YOU',
    'I)SAN'
]

input = list(open('input/day06.txt').read().split())

# PART 1
orbits = {}

for i in input:
    father = i.split(')')[0]
    son = i.split(')')[1]
    orbits[son] = father

count = 0
for key in orbits:
    if key != 'COM':
        tmp_key = key
        while True:
            count += 1
            tmp_key = orbits[tmp_key]
            if tmp_key == 'COM':
                break
print(count)

# PART 2
my_fathers = []
key = 'YOU'
while True:
    key = orbits[key]
    my_fathers.append(key)
    if key == 'COM':
        break

san_fathers = []
key = 'SAN'
while True:
    key = orbits[key]
    san_fathers.append(key)
    if key in my_fathers or key == 'COM':
        break

# print(my_fathers, san_fathers)
print(my_fathers.index(key) + len(san_fathers) - 1)
