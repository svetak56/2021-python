maze_open = open('maze-for-u.txt',"r")
maze = []

for line in maze_open:
    maze.append(line[:-1])


POSSIBLE_WAYS = ('N', 'S', 'W', 'E')
treja_is_found = False

def is_coord_in_maze(maze, coord):
    if coord[0]<0 or coord[0]>len(maze)-1:
        return False
    if coord[1]<0 or coord[1]>len(maze[0])-1:
        return False
    return True

def is_treja_clean(coord):
    global treja_is_here
    if coord[0] == treja_is_here[0] and coord[1] == treja_is_here[1]:
         print('treja_is_here!')
         return True
    else:
        return False

        



def is_coord_exit(coord):
    if coord[0]>9:
        return True
    return False

def is_path_clean(maze, coord):
    if maze[coord[0]][coord[1]] == '#':
        return False
    return True

def step(coord, direction):
    if direction == 'N':
         return step_N(coord)
    elif direction == 'S':
         return step_S(coord)
    elif direction == 'E':
         return step_E(coord)
    elif direction == 'W':
         return step_W(coord)

def step_N(coord):
    return [coord[0]-1, coord[1]]

def step_E(coord):
    return [coord[0], coord[1]+1]

def step_S(coord):
    return [coord[0]+1, coord[1]]

def step_W(coord):
    return [coord[0], coord[1]-1]

def cut_way_back(direction):
    # how to do thing like this:
    # to cancel the way back
    # 'cause strings in python are unmutable
    if direction == "N":
        return ("N","E","W")
    if direction == "S":
        return ("S","E","W")
    if direction == "E":
        return ("N","E","S")
    if direction == "W":
        return ("N","S","W")
    

def find_a_way(maze, coord,possible_ways):
    len_y, len_x = len(maze), len(maze[0])
    global path_to_exit, current_path , treja_is_found
    #print('x: ', len_x, ' y:', len_y)
    #print('Start from: ', coord)

    if not is_coord_in_maze(maze, coord):
        print('not in bounds!')
        return
    
    if len(current_path) > len(path_to_exit):
         print('too large path')
         return
    
    for direction in possible_ways:
        if is_treja_clean(step(coord, direction)) or treja_is_found:
            treja_is_found = True
            return
        else:
            if is_path_clean(maze, step(coord, direction)) :
                print(direction)
                current_path.append(direction)
                find_a_way(maze, step(coord, direction),cut_way_back(direction))
                current_path.pop()
    return 

path_to_exit = []
for i in range(len(maze)*len(maze[0])):
    path_to_exit.append(' ')
               
current_path = []

start_point = [0, 1]
x = int(input("коорд х трежи: "))
y = int(input("коорд y трежи: "))
treja_is_here = (y,x)

find_a_way(maze, start_point,POSSIBLE_WAYS)

print(path_to_exit)
