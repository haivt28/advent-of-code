import re


input = open('input/day18.txt').read()


def calculate_part1(express):
    express = re.sub(r'[()]', '', express).split()
    res = 0
    operator = '+'
    for e in express:
        if e in '+*':
            operator = e
        else:
            if operator == '+':
                res += int(e)
            else:
                res *= int(e)
    return res


def calculate_part2(express):
    while True:  # Calculate all multiplier first
        if re.search(r'\d+[^*\d]+\d+', express):
            for match in re.findall(r'\d+[^*\d]+\d+', express):
                express = express.replace(match, str(calculate_part1(match)), 1)
        else:
            return calculate_part1(express)


def process(calculate_func):
    total = 0
    for line in input.split('\n'):
        while True:
            if re.search(r'\([^()]+\)', line):
                for match in re.findall(r'\([^()]+\)', line):
                    line = line.replace(match, str(calculate_func(match)), 1)
            else:
                total += calculate_func(line)
                break

    return total


# PART 1
print(process(calculate_part1))

# PART 2
print(process(calculate_part2))
