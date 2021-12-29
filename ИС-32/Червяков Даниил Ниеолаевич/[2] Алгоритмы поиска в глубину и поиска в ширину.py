from collections import deque

maze_o = open('maze-for-u.txt',"r")
maze = []

for line in maze_o:
    opened_maze.append(line[:-1])

POSSIBLE_WAYS = ('N', 'S', 'W', 'E')
treja_is_found = False

def coord_in(opened_maze, coord):
    len_y, len_x = len(opened_maze), len(opened_maze[0])
    if coord[0]<0 or coord[0]>len_x :
        return False
    if coord[1]<0 or coord[1]>len_y:
        return False
    return True

def treasure_clean(coord):
    global treasure_here
    if coord[0] == treasure_here[0] and coord[1] == treasure_here[1]:
         print('treasure_is_here!')
         return True
    else:
        return False

def split(s):
    return [char for char in s]     

def exit(coord):
    if coord[0]>9:
        return False
    return True

def path_clean(opened_maze, coord):
    if opened_maze[coord[0]][coord[1]] == '#':
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

def the_way_back(direction):
    if direction == "N":
        return ("N","E","W")
    if direction == "S":
        return ("S","E","W")
    if direction == "E":
        return ("N","E","S")
    if direction == "W":
        return ("N","S","W")


def bfs(opened_maze,coord,t):
    n, m = len(opened_maze), len(opened_maze[0])
    INF =  0
    p = [[None]*m for _ in range(n)]
    d = [[INF]*m for _ in range(n)] 
    used = [[False]*m for _ in range(n)] 
    queue = deque() 
    delta = [(0,-1),(0,1),(1,0),(-1,0)]
    
    d[coord[0]][coord[1]] = 0 
    
    used[coord[0]][coord[1]] = True 
    queue.append(coord)
    while len(queue)!= 0: 
        x,y = queue.popleft() 
        for dx,dy in delta: 
            nx,ny = x + dx, y + dy 

            if 0 <= nx <n and 0 <= ny < m and not used[nx][ny] and opened_maze[nx][ny] != "#": 
                d[nx][ny] = d[x][y] + 1 
                p[nx][ny] = (x,y)
                used[nx][ny] = True 
                queue.append((nx,ny)) 
    print(d[t[0]][t[1]])
    cur = t
    path = []
    while cur is not None:
        path.append(cur)
        cur = p[cur[0]][cur[1]]
    path.reverse()
    count = 0
    
    for i in path:
        ys = path[count][1]
        xs = path[count][0]
        b = split(opened_maze[xs])
        b[ys] = ","
        opened_maze[xs] = ''.join(b)
        count+=1

def find_way(opened_maze, coord,possible_ways):
    
    len_y, len_x = len(opened_maze), len(opened_maze[0])
    global path_to_exit, current_path , treja_is_found 

    if not coord_in(opened_maze, coord):
        print('not in bounds!')
        return
    
    if len(current_path) > len(path_to_exit):
         print('too large path')
         return
    
    for direction in possible_ways:
        if treasure_clean(step(coord, direction)) or treja_is_found:
            treja_is_found = True
            b = split(opened_maze[coord[0]])
            b[coord[1]] = "."
            opened_maze[coord[0]] = ''.join(b)
            
            return  
            
        else:
            if path_clean(opened_maze, step(coord, direction)) :

                current_path.append(direction)
                find_way(opened_maze, step(coord, direction),the_way_back(direction))
                current_path.pop()
                if treja_is_found == False:
                    b = split(opened_maze[coord[0]])
                    b[coord[1]] = "."
                    opened_maze[coord[0]] = ''.join(b)
    return 

path_to_exit = []
for i in range(len(opened_maze)*len(opened_maze[0])):
    path_to_exit.append(' ')
               
current_path = []

start_point = [0, 1]
x = int(input("коорд х трежи: "))
y = int(input("коорд y трежи: "))

coord_point = [y,x]

t_coord = [118,141]

treasure_here = (y,x)

find_way(opened_maze, start_point,POSSIBLE_WAYS)

bfs(opened_maze,coord_point,t_coord)

b = split(opened_maze[y])
b[x] = "*"
opened_maze[y] = ''.join(b)

with open("opened_maze-for-me-done.txt", "w") as txt_file:
    for line in opened_maze:
        txt_file.write(" ".join(line) + "\n")
