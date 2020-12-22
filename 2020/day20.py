import math


def flip_horizontal(tile):
    tile_ = []
    for i in reversed(range(len(tile))):
        tile_.append(tile[i])
    return tile_


def flip_vertical(tile):
    tile_ = []
    for i in range(len(tile)):
        tile_.append(tile[i][::-1])
    return tile_


def rotate_clockwise(tile):
    tile_ = []
    for i in range(len(tile)):
        tile_.append(''.join([tile[j][i] for j in reversed(range(len(tile)))]))
    return tile_


def rotate_counter_clockwise(tile):
    tile_ = []
    for i in reversed(range(len(tile))):
        tile_.append(''.join([tile[j][i] for j in range(len(tile))]))
    return tile_


def check_orientation(tile_id, adj_n, adj_w):
    if adj_n is not None:
        if adj_n == tiles_edges[tile_id][0]:  # north edge
            return True, tiles[tile_id]
        if adj_n == tiles_edges[tile_id][2]:  # south edge
            tile = flip_horizontal(tiles[tile_id])
            return True, tile
        if adj_n == tiles_edges[tile_id][4]:  # west edge
            tile = rotate_counter_clockwise(tiles[tile_id])
            tile = flip_horizontal(tile)
            return True, tile
        if adj_n == tiles_edges[tile_id][6]:  # est edge
            tile = rotate_counter_clockwise(tiles[tile_id])
            return True, tile

        if adj_n == tiles_edges[tile_id][1]:  # reversed north edge
            tile = flip_vertical(tiles[tile_id])
            return True, tile
        if adj_n == tiles_edges[tile_id][3]:  # reversed south edge
            tile = rotate_clockwise(tiles[tile_id])
            tile = rotate_clockwise(tile)
            return True, tile
        if adj_n == tiles_edges[tile_id][5]:  # reversed west edge
            tile = rotate_clockwise(tiles[tile_id])
            return True, tile
        if adj_n == tiles_edges[tile_id][7]:  # reversed est edge
            tile = rotate_counter_clockwise(tiles[tile_id])
            tile = flip_vertical(tile)
            return True, tile
    if adj_w is not None:
        if adj_w == tiles_edges[tile_id][0]:  # north edge
            tile = rotate_counter_clockwise(tiles[tile_id])
            tile = flip_horizontal(tile)
            return True, tile
        if adj_w == tiles_edges[tile_id][2]:  # south edge
            tile = rotate_clockwise(tiles[tile_id])
            return True, tile
        if adj_w == tiles_edges[tile_id][4]:  # west edge
            return True, tiles[tile_id]
        if adj_w == tiles_edges[tile_id][6]:  # est edge
            tile = flip_vertical(tiles[tile_id])
            return True, tile

        if adj_w == tiles_edges[tile_id][1]:  # reversed north edge
            tile = rotate_counter_clockwise(tiles[tile_id])
            return True, tile
        if adj_w == tiles_edges[tile_id][3]:  # reversed south edge
            tile = rotate_clockwise(tiles[tile_id])
            tile = flip_horizontal(tile)
            return True, tile
        if adj_w == tiles_edges[tile_id][5]:  # reversed west edge
            tile = flip_horizontal(tiles[tile_id])
            return True, tile
        if adj_w == tiles_edges[tile_id][7]:  # reversed est edge
            tile = rotate_counter_clockwise(tiles[tile_id])
            tile = rotate_counter_clockwise(tile)
            return True, tile
    return False, None


def find_monster(img):
    monster_count = 0
    for i in range(len(img) - len(monster)):
        for j in range(len(img) - len(monster[0])):
            match = True
            for x in range(len(monster)):
                for y in range(len(monster[0])):
                    if monster[x][y] == '#' and img[i+x][j+y] == '.':
                        match = False
                        break
                if not match:
                    break
            if match:
                monster_count += 1
    return monster_count


def count_sharp(image):
    count = 0
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == '#':
                count += 1
    return count


# PART 1
# I don't try to re-assemble the image in the first part.
# Instead I find the tiles that have exactly 2 edges that don't match any others edges.
# They are the corner tiles, and I just have to multiply them.
input = open('input/day20.txt').read()

tiles = {}
tiles_edges = {}

for line in input.split('\n'):
    if 'Tile' in line:
        tile_id = line.split()[1].replace(':', '')
        tiles[tile_id] = []
    elif line != '':
        tiles[tile_id].append(line)

for k, v in tiles.items():
    edge_n = v[0]
    edge_s = v[len(v)-1]
    edge_w = ''.join([a[0] for a in v])
    edge_e = ''.join([a[len(v)-1] for a in v])

    tiles_edges[k] = [edge_n, edge_n[::-1],
                      edge_s, edge_s[::-1],
                      edge_w, edge_w[::-1],
                      edge_e, edge_e[::-1]]

count_pair_edges = {}
for k, v in tiles_edges.items():
    for edge in v:
        if edge not in count_pair_edges:
            count_pair_edges[edge] = 0
        count_pair_edges[edge] += 1

res = 1
init_tile = ''
for k, v in tiles_edges.items():
    count_sole_edges = 0
    for edge in v:
        if count_pair_edges[edge] == 1:
            count_sole_edges += 1

    if count_sole_edges == 4:
        res *= int(k)
        init_tile = k

print(res)


# PART 2
# After saving all possible edges of each tiles, I can easily re-assemble the image
# from left to right and top to bottom based on the pair edges.
# Then I generate all possible images by rotation and flipping, use the monster as
# a sliding window to check the appearance.
adj_n = ''
if count_pair_edges[tiles_edges[init_tile][0]] == count_pair_edges[tiles_edges[init_tile][6]] == 1:
    adj_n = tiles_edges[init_tile][6]
elif count_pair_edges[tiles_edges[init_tile][6]] == count_pair_edges[tiles_edges[init_tile][2]] == 1:
    adj_n = tiles_edges[init_tile][2]
elif count_pair_edges[tiles_edges[init_tile][2]] == count_pair_edges[tiles_edges[init_tile][4]] == 1:
    adj_n = tiles_edges[init_tile][4]
elif count_pair_edges[tiles_edges[init_tile][4]] == count_pair_edges[tiles_edges[init_tile][0]] == 1:
    adj_n = tiles_edges[init_tile][0]

filled_tiles = []
image = []
image_size = int(math.sqrt(len(tiles)))
for i in range(image_size):
    row = []
    adj_w = ''
    for t_id in tiles:
        if t_id not in filled_tiles:
            is_next_tile, next_tile = check_orientation(t_id, adj_n, None)
            if is_next_tile:
                filled_tiles.append(t_id)
                row.append(next_tile)
                adj_n = next_tile[len(next_tile) - 1]
                adj_w = ''.join([a[len(next_tile) - 1] for a in next_tile])
                break
    for j in range(1, image_size):
        for t_id in tiles:
            if t_id not in filled_tiles:
                is_next_tile, next_tile = check_orientation(t_id, None, adj_w)
                if is_next_tile:
                    filled_tiles.append(t_id)
                    row.append(next_tile)
                    adj_w = ''.join([a[len(next_tile) - 1] for a in next_tile])
                    break
    image.append(row)

normalized_image = []
for i in range(image_size):
    for k in range(1, len(image[i][j]) - 1):
        row = ''
        for j in range(image_size):
            row += image[i][j][k][1:-1]
        normalized_image.append(row)

monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]

all_images = [
    normalized_image,
    rotate_clockwise(normalized_image),
    rotate_counter_clockwise(normalized_image),
    rotate_clockwise(rotate_clockwise(normalized_image)),
    flip_vertical(normalized_image),
    rotate_clockwise(flip_vertical(normalized_image)),
    rotate_counter_clockwise(flip_vertical(normalized_image)),
    rotate_clockwise(rotate_clockwise(flip_vertical(normalized_image))),
]

for img in all_images:
    monster_count = find_monster(img)
    if monster_count > 0:
        print(count_sharp(img) - monster_count*count_sharp(monster))
        break
