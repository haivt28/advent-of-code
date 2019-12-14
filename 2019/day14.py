import math
import copy


def get_remain_materials(react):
    leftside_react = list(react.values())
    leftside_react = [m[1] for m in leftside_react]
    remain_materials = []
    for m in leftside_react:
        remain_materials += m
    remain_materials = set([m[1] for m in remain_materials])
    return remain_materials


# Testcases
data = '''10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL'''

data = '''171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX'''

data = open('input/day14.txt').read()

# PART 1
reactions = {}

for line in data.split('\n'):
    product = line.split('=>')[1].strip().split()
    product = [int(product[0]), product[1]]
    materials = line.split('=>')[0].strip().split(',')
    materials = [[int(m.split()[0]), m.split()[1]] for m in materials]
    reactions[product[1]] = [product[0], materials]

reactions_cpy = copy.copy(reactions)
last_react = reactions['FUEL'][1]
reactions.pop('FUEL', None)
last_materials = {}

for r in last_react:
    last_materials[r[1]] = r[0]

while True:
    remain_materials = get_remain_materials(reactions)
    if len(remain_materials) <= 0:
        break

    for m in last_materials:
        if m not in remain_materials:
            require_quantity = last_materials[m]
            react_material = reactions[m][1]
            react_quantity = reactions[m][0]

            ratio = math.ceil(require_quantity / react_quantity) if require_quantity > react_quantity else 1
            for rm in react_material:
                if rm[1] in last_materials:
                    last_materials[rm[1]] += rm[0] * ratio
                else:
                    last_materials[rm[1]] = rm[0] * ratio
            last_materials.pop(m, None)
            reactions.pop(m, None)
            break

print(last_materials)

# PART 2
# Here I use a small cheat to quickly reach the result:
# The step of the last_quantity is increased to 1000 each loop to reduce calculations
# Then the random lower number is choose and reset the step to 1
ore = 1000000000000
last_quantity = 1376000

while True:
    current_reactions = copy.copy(reactions_cpy)
    last_react = current_reactions['FUEL'][1]
    current_reactions.pop('FUEL', None)
    last_materials = {}

    for r in last_react:
        last_materials[r[1]] = r[0] * last_quantity

    while True:
        remain_materials = get_remain_materials(current_reactions)
        if len(remain_materials) <= 0:
            break

        for m in last_materials:
            if m not in remain_materials:
                require_quantity = last_materials[m]
                react_material = current_reactions[m][1]
                react_quantity = current_reactions[m][0]

                ratio = math.ceil(require_quantity / react_quantity) if require_quantity > react_quantity else 1
                for rm in react_material:
                    if rm[1] in last_materials:
                        last_materials[rm[1]] += rm[0] * ratio
                    else:
                        last_materials[rm[1]] = rm[0] * ratio
                last_materials.pop(m, None)
                current_reactions.pop(m, None)
                break

    # print(last_materials)
    if ore < last_materials['ORE']:
        break
    else:
        last_quantity += 1

print(last_quantity-1)
