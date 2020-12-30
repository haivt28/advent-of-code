import queue
import re


def print_maze(maze):
    print('\n'.join([''.join(a) for a in maze]))


def calculate_distance_dict(start_key, maze, cur_x, cur_y):
    if start_key not in distance_dict:
        distance_dict[start_key] = []

    maze_queue = queue.Queue()
    maze_queue.put([cur_x, cur_y, [], 0, ''])
    visited_nodes = [[cur_x, cur_y]]

    while not maze_queue.empty():
        node = maze_queue.get()
        path_to_node = node[2]  # Movement command: 1: North | 2: South | 3: West | 4: East
        length_to_node = node[3]

        child_nodes = [
            [[node[0], node[1] + 1], 1, 2],  # [child_node_position, movement, opposite_movement]
            [[node[0], node[1] - 1], 2, 1],
            [[node[0] - 1, node[1]], 3, 4],
            [[node[0] + 1, node[1]], 4, 3]
        ]

        for child_node in child_nodes:
            if child_node[0] not in visited_nodes:
                movement = child_node[1]
                opposite_mv = child_node[2]
                gates = node[4]

                if len(path_to_node) == 0 or (len(path_to_node) > 0 and path_to_node[-1] != opposite_mv):
                    child_node_val = maze[child_node[0][1]][child_node[0][0]]
                    if re.match(r'[a-z]', child_node_val):
                        distance_dict[start_key].append((child_node_val, length_to_node + 1, set(gates)))
                        if start_key + child_node_val not in distance_dict_short:
                            distance_dict_short[start_key + child_node_val] = length_to_node + 1
                        if child_node_val + start_key not in distance_dict_short:
                            distance_dict_short[child_node_val + start_key] = length_to_node + 1
                    if re.match(r'[A-Z]', child_node_val):
                        gates += child_node_val.lower()
                    if re.match(r'[^#]', child_node_val):
                        maze_queue.put(
                            [child_node[0][0], child_node[0][1], path_to_node + [movement], length_to_node + 1, gates])
                        visited_nodes.append(child_node[0])


def distance_to_get_keys(start_key, remain_keys):
    key_list = distance_dict[start_key]

    if len(remain_keys) <= 0:
        return 0

    cache_key = (start_key, ''.join(list(remain_keys)))
    if cache_key in cache:
        return cache[cache_key]

    local_min_step = 100000000
    for key in key_list:
        required_keys = key[2]
        if key[0] not in remain_keys:  # key already taken
            continue
        if len(required_keys) > 0 and len(required_keys & remain_keys) > 0:
            continue
        remain_keys.remove(key[0])
        step_count = distance_dict_short[start_key + key[0]] + distance_to_get_keys(key[0], remain_keys)
        remain_keys.add(key[0])

        local_min_step = min(local_min_step, step_count)

    cache[cache_key] = local_min_step

    return local_min_step


# PART 1
data = '''#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################'''
data = open('input/day18.txt').read()

distance_dict = {}
distance_dict_short = {}
all_keys = set(re.sub(r'[#.A-Z\s]', '', data))
maze = []
cur_x = 0
cur_y = 0
for line in data.split():
    maze.append(list(line))
# print_maze(maze)

for key in all_keys:
    for line in data.split():
        if key in line:
            cur_x = line.index(key)
            cur_y = data.split().index(line)
    calculate_distance_dict(key, maze, cur_x, cur_y)

cache = {}
all_keys.remove('@')
print(distance_to_get_keys('@', all_keys))

# PART 2
# Here I solved part 2 by calculate min steps in each quadrant and
# ignore gates that don't have keys in corresponded quadrant
data1 = '''#############
#DcBa.#.GhKl#
#.###...#I###
#e#d#.@.#j#k#
###C#...###J#
#fEbA.#.FgHi#
#############'''

distance_dict.clear()
distance_dict_short.clear()
all_keys = set(re.sub(r'[#.A-Z\s]', '', data))
maze = []
cur_x = 0
cur_y = 0
for line in data.split():
    maze.append(list(line))

mid_x = len(maze)//2
mid_y = len(maze[mid_x])//2
maze[mid_x-1][mid_y-1:mid_y+2] = ['@', '#', '%']
maze[mid_x+0][mid_y-1:mid_y+2] = ['#', '#', '#']
maze[mid_x+1][mid_y-1:mid_y+2] = ['$', '#', '&']
all_keys.update(['%', '&', '$'])
# print_maze(maze)

for key in all_keys:
    for line in maze:
        if key in line:
            cur_x = line.index(key)
            cur_y = maze.index(line)
    calculate_distance_dict(key, maze, cur_x, cur_y)

cache.clear()
min_step = 0
for robot in ['@', '%', '&', '$']:
    remain_in_section = set()
    for key in distance_dict[robot]:
        remain_in_section.add(key[0])
    min_step += distance_to_get_keys(robot, remain_in_section)

print(min_step)
