maze_open = open('maze-for-u.txt',"r")
maze = []

for line in maze_open:
    maze.append(line[:-1])

print(maze)


