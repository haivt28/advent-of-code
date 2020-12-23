import re


def generate_pattern(rule):
    pattern = rule['0']
    while re.search(r'\d', pattern):
        pattern_list = pattern.split()
        for i in range(len(pattern_list)):
            if pattern_list[i] in rule:
                pattern_list[i] = rule[pattern_list[i]]
                if pattern_list[i] not in 'ab':
                    pattern_list[i] = '( ' + pattern_list[i] + ' )'
        pattern = ''.join(pattern_list)
    return pattern


input = open('input/day19.txt').read()


rule_map = {}
pattern_part1 = ''
pattern_part2 = ''
done_init = False
count_part1 = 0
count_part2 = 0

for line in input.split('\n'):
    if line == '':
        pattern_part1 = generate_pattern(rule_map)

        # Here I tricked part 2 by generate a limited loops for rule 8 and rule 11
        rule_8_update = rule_map['8']
        rule_11_update = rule_map['11']
        for i in range(2, 10):
            rule_8_update += ' | ' + ' '.join([rule_map['8']] * i)
            rule_11_update += ' | ' + \
                              ' '.join([rule_map['11'].split()[0]] * i) + ' ' + \
                              ' '.join([rule_map['11'].split()[1]] * i)
        rule_map['8'] = rule_8_update
        rule_map['11'] = rule_11_update
        pattern_part2 = generate_pattern(rule_map)

        done_init = True
        continue

    if not done_init:
        rule_index = line.split(':')[0]
        rule = line.split(':')[1].strip().replace('"', '')
        rule_map[rule_index] = rule
    else:
        if re.search(r'^' + pattern_part1 + r'$', line):
            count_part1 += 1
        if re.search(r'^' + pattern_part2 + r'$', line):
            count_part2 += 1

# PART 1
print(count_part1)

# PART 2
print(count_part2)
