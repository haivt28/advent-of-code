import copy

input = open('input/day21.txt').read()


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


foods = []
for line in input.split('\n'):
    ingredients = line.split('(')[0].strip().split()
    allergens = line.split('(')[1].replace(')', '').replace(',', '').replace('contains ', '').split()

    foods.append([ingredients, allergens])


tmp = copy.deepcopy(foods)
allergens = []
while True:
    new_list = []
    is_break = False
    for i in range(len(foods) - 1):
        for j in range(i + 1, len(foods)):
            intersec_ingr = intersection(foods[i][0], foods[j][0])
            intersec_alle = intersection(foods[i][1], foods[j][1])

            if len(intersec_ingr) == len(intersec_alle) == 1:
                allergens.append((intersec_alle[0], intersec_ingr[0]))
                foods = tmp
                new_list = []
                for x in range(len(foods)):
                    if intersec_ingr[0] in foods[x][0]:
                        foods[x][0].remove(intersec_ingr[0])
                    if intersec_alle[0] in foods[x][1]:
                        foods[x][1].remove(intersec_alle[0])
                is_break = True
                tmp = copy.deepcopy(foods)
                break
            elif len(intersec_ingr) >= 1 and len(intersec_alle) >= 1:
                new_list.append([intersec_ingr, intersec_alle])
        if is_break:
            break

    foods.extend(new_list)

    remain_alle = [item for sublist in [food[1] for food in foods] for item in sublist]
    if len(remain_alle) <= 0:
        break


# PART 1
remain_ingr = [item for sublist in [food[0] for food in foods] for item in sublist]
print(len(remain_ingr))

# PART 2
print(','.join([a[1] for a in sorted(allergens, key=lambda x: x[0])]))
