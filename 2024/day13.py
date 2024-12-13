import re

report = list(map(str, open('input/day13.txt').read().split('\n')))

ax = 0
ay = 0
bx = 0
by = 0
px = 0
py = 0
total_token = 0
total_token2 = 0


def calculate(ax, ay, bx, by, px, py):
    nA = 0.0
    nB = 0.0
    if ax / ay != bx / by:
        nB = (ax * py - ay * px) / (0 - ay * bx + ax * by)
        nA = (px - bx * nB) / ax

    return nA, nB


for line in report:
    if 'Button A' in line:
        ax = int(re.findall(r'X\+\d+', line)[0].replace('X+', ''))
        ay = int(re.findall(r'Y\+\d+', line)[0].replace('Y+', ''))
    elif 'Button B' in line:
        bx = int(re.findall(r'X\+\d+', line)[0].replace('X+', ''))
        by = int(re.findall(r'Y\+\d+', line)[0].replace('Y+', ''))
    elif 'Prize' in line:
        px = int(re.findall(r'X=\d+', line)[0].replace('X=', ''))
        py = int(re.findall(r'Y=\d+', line)[0].replace('Y=', ''))

        # PART 1
        nA, nB = calculate(ax, ay, bx, by, px, py)
        if nA.is_integer() and nB.is_integer() and nA <= 100 and nB <= 100:
            total_token += 3 * int(nA) + int(nB)

        # PART 2
        nA2, nB2 = calculate(ax, ay, bx, by, px + 10000000000000, py + 10000000000000)
        if nA2.is_integer() and nB2.is_integer():
            total_token2 += 3 * int(nA2) + int(nB2)

print(total_token)
print(total_token2)