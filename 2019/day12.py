import numpy as np
import math


input = '''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''

input = '''<x=5, y=13, z=-3>
<x=18, y=-7, z=13>
<x=16, y=3, z=4>
<x=0, y=8, z=8>'''

# PART 1
pos = []
vel = []

for line in input.split('\n'):
    x = int(line.split(',')[0].split('=')[1])
    y = int(line.split(',')[1].split('=')[1])
    z = int(line.split(',')[2].split('=')[1][:-1])
    pos.append([x, y, z])
    vel.append([0, 0, 0])

for step in range(1000):
    for i in range(len(pos)):
        for j in range(1, len(pos)):
            if j > i:
                if pos[i][0] < pos[j][0]:
                    vel[i][0] += 1
                    vel[j][0] -= 1
                elif pos[i][0] > pos[j][0]:
                    vel[i][0] -= 1
                    vel[j][0] += 1

                if pos[i][1] < pos[j][1]:
                    vel[i][1] += 1
                    vel[j][1] -= 1
                elif pos[i][1] > pos[j][1]:
                    vel[i][1] -= 1
                    vel[j][1] += 1

                if pos[i][2] < pos[j][2]:
                    vel[i][2] += 1
                    vel[j][2] -= 1
                elif pos[i][2] > pos[j][2]:
                    vel[i][2] -= 1
                    vel[j][2] += 1

        pos[i][0] += vel[i][0]
        pos[i][1] += vel[i][1]
        pos[i][2] += vel[i][2]


total = 0
for i in range(len(pos)):
    pot = abs(pos[i][0]) + abs(pos[i][1]) + abs(pos[i][2])
    kin = abs(vel[i][0]) + abs(vel[i][1]) + abs(vel[i][2])
    total += pot * kin

print(total)


# PART 2
# All coordinates cannot be calculated simultaneously
# The cycle of each coordinate is calculated separately then find the LCM of them to get the whole 3D cycle

# Least Common Multiple
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


pos_x = []
pos_y = []
pos_z = []
vel = []

for line in input.split('\n'):
    x = int(line.split(',')[0].split('=')[1])
    y = int(line.split(',')[1].split('=')[1])
    z = int(line.split(',')[2].split('=')[1][:-1])
    pos_x.append(x)
    pos_y.append(y)
    pos_z.append(z)
    vel.append(0)

pos = np.array([pos_x, pos_y, pos_z])
pos0 = np.array([pos_x, pos_y, pos_z])
vel = np.array([vel, vel, vel])
vel0 = np.array([vel, vel, vel])

count = [0, 0, 0]
for id_coor in range(len(pos)):
    while True:
        vel_dif = np.array([
            np.sign(pos[id_coor][1] - pos[id_coor][0]) +
            np.sign(pos[id_coor][2] - pos[id_coor][0]) +
            np.sign(pos[id_coor][3] - pos[id_coor][0]),

            np.sign(pos[id_coor][0] - pos[id_coor][1]) +
            np.sign(pos[id_coor][2] - pos[id_coor][1]) +
            np.sign(pos[id_coor][3] - pos[id_coor][1]),

            np.sign(pos[id_coor][0] - pos[id_coor][2]) +
            np.sign(pos[id_coor][1] - pos[id_coor][2]) +
            np.sign(pos[id_coor][3] - pos[id_coor][2]),

            np.sign(pos[id_coor][0] - pos[id_coor][3]) +
            np.sign(pos[id_coor][1] - pos[id_coor][3]) +
            np.sign(pos[id_coor][2] - pos[id_coor][3])
        ])

        vel[id_coor] += vel_dif
        pos[id_coor] += vel[id_coor]

        count[id_coor] += 1
        if (pos[id_coor] == pos0[id_coor]).all() and (vel[id_coor] == vel0[id_coor]).all():
            break

print(count)
print(lcm(count[0], lcm(count[1], count[2])))
