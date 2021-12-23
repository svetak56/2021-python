from collections import deque

POSSIBLE_WAYS = ('N', 'S', 'W', 'E')
FILE_TO_READ = 'lab.txt'

class Maze:
    maze = []
    path_to_exit = []
    current_path = []
    tresure_is_found = False
    start_point = [0, 1]
    x = int(input("коорд х: "))
    y = int(input("коорд y: "))
    coord_point = [y, x]
    t_coord = [118, 141]
    tresure_is_here = (y, x)
    def read(self):
        for line in open(FILE_TO_READ, "r"):
            self.maze.append(line[:-1])
        for i in range(len(self.maze)*len(self.maze[0])):
            self.path_to_exit.append(' ')


 classPathfinder:
     defstep(self,coord, direction):
        if direction == 'N':
            return self.step_N(coord)
         elifdirection == 'S':
            return self.step_S(coord)
         elifdirection == 'E':
            return self.step_E(coord)
         elifdirection == 'W':
            return self.step_W(coord)

    def step_N(self,coord):
        return [coord[0]-1, coord[1]]

    def step_E(self,coord):
        return [coord[0], coord[1]+1]

    def step_S(self,coord):
        return [coord[0]+1, coord[1]]

    def step_W(self,coord):
        return [coord[0], coord[1]-1]

    def is_coord_in_maze(self, maze, coord):
        len_y, len_x = len(maze), len(maze[0])
        if coord[0] < 0 or coord[0] > len_x:
            return False
        if coord[1] < 0 or coord[1] > len_y:
            return False
        return True

    def is_tresure_clean(self,coord, tresure_is_here ):
        if coord[0] == tresure_is_here[0] and coord[1] == tresure_is_here[1]:
            print('tresure_is_here!')
            return True
        else:
            return False

    def split(self,s):
        return [char for char in s]

    def is_path_clean(self,maze, coord):
        if maze[coord[0]][coord[1]] == '#':
            return False
        return True

    def cut_way_back(self,direction):
        if direction == "N":
            return ("N", "E", "W")
        if direction == "S":
            return ("S", "E", "W")
        if direction == "E":
            return ("N", "E", "S")
        if direction == "W":
            return ("N", "S", "W")

    def find_a_way(self, maze, coord, possible_ways, path_to_exit, current_path, tresure_is_found, tresure_is_here):

        if not self.is_coord_in_maze(maze, coord):
            print('вне зоны!')
            return

        if len(current_path) > len(path_to_exit):
            print('слишком длинный путь')
            return

        for direction in possible_ways:
            if self.is_tresure_clean(self.step(coord, direction), tresure_is_here) or tresure_is_found:
                tresure_is_found = True

                b = self.split(maze[coord[0]])
                b[coord[1]] = "."
                maze[coord[0]] = ''.join(b)

                return

            else:
                if self.is_path_clean(maze, self.step(coord, direction)):

                    current_path.append(direction)
                    self.find_a_way(maze, self.step(coord, direction),
                               self.cut_way_back(direction), path_to_exit, current_path, tresure_is_found, tresure_is_here)
                    current_path.pop()
                    if tresure_is_found == False:
                        b = self.split(maze[coord[0]])
                        b[coord[1]] = "."
                        maze[coord[0]] = ''.join(b)
        return


class Tracer:
    def bfs(maze, coord, t):
        try:
            n, m = len(maze), len(maze[0])
            INF = 0
            p = [[None]*m for _ in range(n)]
            d = [[INF]*m for _ in range(n)]
            used = [[False]*m for _ in range(n)]
            queue = deque()
            delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]

            d[coord[0]][coord[1]] = 0

            used[coord[0]][coord[1]] = True
            queue.append(coord)
            while len(queue) != 0:
                x, y = queue.popleft()
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < m and not used[nx][ny] and maze[nx][ny] != "#":

                        d[nx][ny] = d[x][y] + 1
                        p[nx][ny] = (x, y)
                        used[nx][ny] = True
                        queue.append((nx, ny))
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
                b = Pathfinder.split(maze[xs])
                b[ys] = ","
                maze[xs] = ''.join(b)
                count += 1
        except IndexError:
            pass


class Trace_maker:
    def write(maze,p,x,y):
        b = Pathfinder.split(p,maze[y])
        b[x] = "*"
        maze[y] = ''.join(b)

        with open("maze-for-me-done.txt", "w") as txt_file:
            for line in maze:
                txt_file.write(" ".join(line) + "\n")


if __name__ == "__main__":

    m = Maze()
    m.read()
    p = Pathfinder()
    Pathfinder.find_a_way(p,m.maze, m.start_point, POSSIBLE_WAYS, m.path_to_exit, m.current_path, m.tresure_is_found, m.tresure_is_here)
    Tracer.bfs(m.maze, m.coord_point, m.t_coord)
    Trace_maker.write(m.maze,p,m.x,m.y)