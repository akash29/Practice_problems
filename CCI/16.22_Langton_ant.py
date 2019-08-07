import random

size = 5
direction = {
    "east": "south",
    "south": "west",
    "west": "north",
    "north": "east"
}

direction_id_map = {
    "east": [0, 1],
    "south": [1, 0],
    "west": [0, -1],
    "north": [-1,0]
}


def get_new_position(i, j, id_list):
    new_i = i + id_list[0]
    new_j = j+id_list[1]
    if new_i == -1 or new_i == 5:
        new_i = i
    if new_j == -1 or new_j == 5:
        new_j = j
    return new_i, new_j


def clockwise(pos):
    return rotate(pos,1)


def counter_clockwise(pos):
    return rotate(pos,3)


def rotate(pos, times):
    if times == 0:
        return pos
    elif times > 0:
        return rotate(direction[pos],times-1)


def construct_grid():
    start_mat = [[1 if i % 2 == 0 else 0 for i in range(size)] for j in range(size)]
    compl_mat = start_mat[:]
    for i in range(0, len(start_mat), 2):
        for j in range(len(start_mat[i])):
            compl_mat[i][j] = 1-start_mat[i][j]
    return compl_mat


def get_position():
    return [random.randint(0, size-1), random.randint(0, size-1)]


def print_k_moves(k):
    i, j = get_position()
    print ("Initial grid position:{0},{1}".format(i,j))
    initial_position = "east"  # right
    print ("Initial position:", initial_position)
    while k > 0:
        if grid[i][j] == 0:  # if grid elem is white
            grid[i][j] = 1
            initial_position = clockwise(initial_position)
            temp_l = direction_id_map[initial_position]
            i,j = get_new_position(i,j,temp_l)

        elif grid[i][j] == 1:  # if grid elem is black
            grid[i][j] = 0
            initial_position = counter_clockwise(initial_position)
            temp_l = direction_id_map[initial_position]
            i,j = get_new_position(i,j,temp_l)
        print(grid)
        k -= 1


grid = construct_grid()
print_k_moves(3)


