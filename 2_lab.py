maze = ('######## #',
        '#  #   # #',
        '## # ### #',
        '##   #   #',
        '#  ##  ###',
        '##     # #',
        '# ## ### #',
        '# ## # # #',
        '####     #',
        '####### ##', 
        '####### ##')

path_to_exit = [' '*len(maze)*len(maze[0])]
current_path = []

def is_coord_in_maze(coord):
    if coord[0]<0 | coord[0]>len(maze)-1:
        return False
    if coord[1]<0 | coord[1]>len(maze[0])-1:
        return False
    return True

def is_coord_exit(coord):
    if coord[0]>9:
        return True
    return False

def step_N(coord):
    return [coord[0]-1, coord[1]]

def step_E(coord):
    return [coord[0], coord[1]+1]

def step_S(coord):
    return [coord[0]+1, coord[1]]

def step_W(coord):
    return [coord[0], coord[1]-1]

def path_is_clean(coord):
    if maze[coord[0]][coord[1]] == '#':
        return False
    return True

def find_a_way(maze, coord):
    len_y, len_x = len(maze), len(maze[0])
    #print('x: ', len_x, ' y:', len_y)
    #print('Start from: ', coord)

    if ~is_coord_in_maze(coord):
        return

    if len(current_path) > len(path_to_exit):
        return

    if is_coord_exit(coord):
        path_to_exit = current_path.copy()
        return

    if path_is_clean(step_N(coord)):
        new_coord = step_N(coord)
        current_path.append('N')
        find_a_way(maze, new_coord)
        current_path.pop()

    if path_is_clean(step_E(coord)):
        new_coord = step_E(coord)
        current_path.append('E')
        find_a_way(maze, new_coord)
        current_path.pop()

    if path_is_clean(step_S(coord)): 
        new_coord = step_S(coord)
        current_path.append('S')
        find_a_way(maze, new_coord)
        current_path.pop()

    if path_is_clean(step_W(coord)):
        new_coord = step_W(coord)
        current_path.append('W')
        find_a_way(maze, new_coord)
        current_path.pop()

    return 0


print(maze[0][8])
find_a_way(maze, [0, 8])

print(path_to_exit)
