DIRECTIONS = ['se', 'sw', 'ne', 'nw', 'e', 'w']


def get_neighbour(tile, direction):
    if direction == 'se':
        return [tile[0] + 1, tile[1] - 2]
    if direction == 'sw':
        return [tile[0] - 1, tile[1] - 2]
    if direction == 'ne':
        return [tile[0] + 1, tile[1] + 2]
    if direction == 'nw':
        return [tile[0] - 1, tile[1] + 2]
    if direction == 'e':
        return [tile[0] + 2, tile[1]]
    if direction == 'w':
        return [tile[0] - 2, tile[1]]


def get_id(tile):
    return str(tile[0]) + ';' + str(tile[1])


def parse_id(tile_id):
    return [int(tile_id.split(';')[0]), int(tile_id.split(';')[1])]


def count_black_neighbours(tile):
    cnt = 0
    for direction in DIRECTIONS:
        tile_id = get_id(get_neighbour(tile, direction))
        if tile_id in tiles and tiles[tile_id] == 1:
            cnt += 1
    return cnt


def get_white_neighbours(tile):
    neighbours = []
    for direction in DIRECTIONS:
        tile_id = get_id(get_neighbour(tile, direction))
        if (tile_id in tiles and tiles[tile_id] == 0) or tile_id not in tiles:
            neighbours.append(tile_id)
    return neighbours


# PART 1
input = open('input/day24.txt').read()
tiles = {}
for line in input.split('\n'):
    next_tile = [0, 0]
    while line != '':
        for direction in DIRECTIONS:
            if line.startswith(direction):
                line = line.replace(direction, '', 1)
                next_tile = get_neighbour(next_tile, direction)
                break

    dest_tile = get_id(next_tile)
    if dest_tile not in tiles:
        tiles[dest_tile] = 1
    else:
        tiles[dest_tile] = 1 - tiles[dest_tile]

print(sum(tiles.values()))


# PART 2
next_tiles = {}
for _ in range(100):
    neighbours = set()
    for k, v in tiles.items():
        next_tiles[k] = v
        if v == 1:
            count_black = count_black_neighbours(parse_id(k))
            if count_black > 2 or count_black == 0:
                next_tiles[k] = 0
            neighbours.update(get_white_neighbours(parse_id(k)))

    for id in neighbours:
        if count_black_neighbours(parse_id(id)) == 2:
            next_tiles[id] = 1

    for k, v in next_tiles.items():
        tiles[k] = v

print(sum(tiles.values()))
