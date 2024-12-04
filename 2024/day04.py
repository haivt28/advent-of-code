report = list(map(str, open('input/day04.txt').read().split('\n')))

w = []
for line in report:
    level = list(line)
    w.append(level)


# PART 1
counter = 0
for i, x in enumerate(w):
    for j, y in enumerate(w[i]):
        if w[i][j] == 'X':
            if (j+3 < len(w[i]) and
                    [w[i][j+1], w[i][j+2], w[i][j+3]] == ['M', 'A', 'S']): counter += 1
            if (j-3 >= 0 and
                    [w[i][j-1], w[i][j-2], w[i][j-3]] == ['M', 'A', 'S']): counter += 1
            if (i+3 < len(w) and
                    [w[i+1][j], w[i+2][j], w[i+3][j]] == ['M', 'A', 'S']): counter += 1
            if (i-3 >= 0 and
                    [w[i-1][j], w[i-2][j], w[i-3][j]] == ['M', 'A', 'S']): counter += 1
            if (i+3 < len(w) and j+3 < len(w[i]) and
                    [w[i+1][j+1], w[i+2][j+2], w[i+3][j+3]] == ['M', 'A', 'S']): counter += 1
            if (i+3 < len(w) and j-3 >= 0 and
                    [w[i+1][j-1], w[i+2][j-2], w[i+3][j-3]] == ['M', 'A', 'S']): counter += 1
            if (i-3 >= 0 and j+3 < len(w[i]) and
                    [w[i-1][j+1], w[i-2][j+2], w[i-3][j+3]] == ['M', 'A', 'S']): counter += 1
            if (i-3 >= 0 and j-3 >= 0 and
                    [w[i-1][j-1], w[i-2][j-2], w[i-3][j-3]] == ['M', 'A', 'S']): counter += 1

print(counter)


# PART 2
counter = 0
for i, x in enumerate(w):
    for j, y in enumerate(w[i]):
        if w[i][j] == 'A' and 0 < i < len(w)-1 and 0 < j < len(w[i])-1:
            if [w[i-1][j-1], w[i+1][j+1]] == [w[i+1][j-1], w[i-1][j+1]] == ['M', 'S']: counter += 1
            if [w[i-1][j-1], w[i+1][j+1]] == [w[i-1][j+1], w[i+1][j-1]] == ['M', 'S']: counter += 1
            if [w[i+1][j+1], w[i-1][j-1]] == [w[i+1][j-1], w[i-1][j+1]] == ['M', 'S']: counter += 1
            if [w[i+1][j+1], w[i-1][j-1]] == [w[i-1][j+1], w[i+1][j-1]] == ['M', 'S']: counter += 1

print(counter)