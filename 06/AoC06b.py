from AoC06a import * 

def count_positions_of_obstacles(i, index, matrix=matrix):
    x1 = index[0][i]
    y1 = index[1][i]

    x2 = x1 + 1
    if x2 in index[0]:
        position_x2 = np.where(index[0] == x2)[0]
        y2 = index[1][position_x2][0]

        y3 = y2 - 1
        if y3 in index[1]:
            position_y3 = np.where(index[1] == y3)[0]
            x3 = index[0][position_y3][0]

            x4 = x3 - 1
            y4 = y3 - 1

            if matrix[x4][y4] in ['X', '>']:
                matrix[x4][y4] = 'O'


count = 0
for i in range(100):
    a = myarray(matrix)
    index = a.index("#")
    for k in range(len(index[0])):
        count_positions_of_obstacles(k, index)
    matrix = np.rot90(matrix)

unique, counts = np.unique(a, return_counts=True)
print(dict(zip(unique, counts)))