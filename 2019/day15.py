from day09 import intcode_computer
import queue


def update_droid(ip_output):
    global is_wall, is_oxygen

    if ip_output == 0:
        is_wall = True
        return 'HALT'

    if ip_output == 2:
        if not is_oxygen:
            is_oxygen = True
            return 'HALT'

    return None


def update_oxygen_info(path, loc):
    global maze_queue, oxygen_path, oxygen_loc, visited_nodes

    oxygen_path = path
    oxygen_loc = loc
    maze_queue = queue.Queue()
    with maze_queue.mutex:
        maze_queue.queue.clear()
    maze_queue.put([oxygen_loc[0], oxygen_loc[1], [], 0])
    print('Path to oxygen:', len(oxygen_path))
    visited_nodes = [[oxygen_loc[0], oxygen_loc[1]]]


ins = list(map(int, open('input/day15.txt').read().split(',')))

# PART 1 + PART 2 can be merged
# Here I use the BFS to find the shortest path to oxygen location
# With part 2, I take advantage of the robot to calculate filling time of oxygen
# The init movements of robot to set to the oxygen location,
# then reset the parameter and performing the BFS again to find all path of the maze
maze_queue = queue.Queue()

maze_queue.put([0, 0, [], 0])
visited_nodes = [[0, 0]]

is_wall = False
is_oxygen = False

oxygen_loc = None
oxygen_path = []

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

            if len(path_to_node) == 0 or (len(path_to_node) > 0 and path_to_node[-1] != opposite_mv):
                intcode_computer(ins, oxygen_path + path_to_node + [movement], update_droid)
                if is_oxygen and oxygen_loc is None:
                    update_oxygen_info(path_to_node + [movement], child_node[0])
                    break
                if not is_wall:
                    maze_queue.put([child_node[0][0], child_node[0][1], path_to_node + [movement], length_to_node + 1])
                    visited_nodes.append(child_node[0])
                is_wall = False

print('Time to fill oxygen:', length_to_node)
