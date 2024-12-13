report = list(map(str, open('input/day10.txt').read().split('\n')))

topo = []
trailheads = []
for line in report:
    level = list(line)
    topo.append(level)
    for id in range(len(level)):
        if level[id] == '0':
            trailheads.append([topo.index(level), id])

rating = 0

def find_top(t_map, current_point, score):
    global rating
    current_height = int(t_map[current_point[0]][current_point[1]])
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for d in directions:
        if 0 <= current_point[0] + d[0] < len(t_map) and 0 <= current_point[1] + d[1] < len(t_map[0]):
            next_point = [current_point[0] + d[0], current_point[1] + d[1]]
            next_height = int(t_map[next_point[0]][next_point[1]])
            if next_height == current_height + 1:
                if next_height == 9:
                    score.add(tuple(next_point))
                    rating += 1
                else:
                    find_top(t_map, next_point, score)

# PART 1 & 2
total_score = 0
for head in trailheads:
    score = set()
    find_top(topo, head, score)
    total_score += len(score)

print(total_score)
print(rating)
