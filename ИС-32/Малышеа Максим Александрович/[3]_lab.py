class Maze:

    def __init__(self):
        self.maze = []
    
    def read_from_file(self):
        maze_open = open("maze-for-u.txt","r")
        for line in maze_open:
            self.maze.append(line[:-1])
            
    def print_maze(self):
        return self.maze

    def place_tresaure(self,x,y):
        b = split(print_maze()[y])
        b[x] = "*"
        print_maze()[y] = ''.join(b)
        

        
    #def save_to_file()
    #def is_cell_clear()
    #def max_x()
    #def max_y()


class Treasure:

    def __init__(self,x,y):
        coord = [x,y]
        is_found = False


        

    
maze = Maze()
maze.read_from_file()

path_to_exit = []
for i in range(len(maze.print_maze())*len(maze.print_maze()[0])):
    path_to_exit.append(' ')
               
current_path = []
start_point = [0, 1]
x = int(input("коорд х трежи: "))
y = int(input("коорд y трежи: "))

treasure = Treasure(x,y)

maze.place_tresaure(x,y)

print(maze.print_maze())





