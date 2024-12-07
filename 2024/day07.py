report = list(map(str, open('input/day07.txt').read().split('\n')))


def convert_to_base(n, base):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, base)
        nums.append(str(r))
    return ''.join(nums)


def is_match_value(value, numbers, base):
    operators = ''.join(str(x) for x in [base-1] * (len(numbers) - 1))
    max_operator_count = int(operators, base)

    for op in reversed(range(max_operator_count + 1)):
        operator = ('{' + '0:0{}'.format(len(operators)) + '}').format(convert_to_base(op, base))

        test_value = numbers[0]
        for id in range(len(numbers) - 1):
            if operator[id] == '0':
                test_value += numbers[id + 1]
            elif operator[id] == '1':
                test_value *= numbers[id + 1]
            else:
                test_value = int(str(test_value) + str(numbers[id + 1]))

            if test_value > value:
                break

        if test_value == value:
            return True

    return False

total_1 = 0
total_2 = 0
for line in report:
    value = int(line.split(':')[0])
    numbers = list(map(int, line.split(':')[1].split()))

    # PART 1
    if is_match_value(value, numbers, base=2):
        total_1 += value
        total_2 += value

    # PART 2
    elif is_match_value(value, numbers, base=3):
        total_2 += value

print(total_1)
print(total_2)