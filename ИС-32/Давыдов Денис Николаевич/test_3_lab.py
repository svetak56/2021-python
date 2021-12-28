
class Maze():
    """ Считывание из файла, хранение, информация о содержимом клетки по координатам, информация о координатах сокровища."""
    def __init__(self, mazer):
        self.mazer = mazer
        #self.sod_klet = sod_klet
        #self.treasure_coord = treasure_coord

    def print_maze(self):
        """Просто вывод лабиринта"""
        print(self.mazer)

    """def read_maze(self):
            Считывание из файла и хранение в maze
        f = open("E:/GitHub/2021-python/ИС-32/Давыдов Денис Николаевич/maze-for-u.txt", "r")
        maze = []
        for line in f:
            maze.append(line[:-1])"""  # Не робит

f = open("E:/GitHub/2021-python/ИС-32/Давыдов Денис Николаевич/maze-for-u.txt", "r")
maze = []
for line in f:
    maze.append(line[:-1])

maze_file = Maze(maze)
maze_file.print_maze()

class Pathfinder():
    """ Информация о личности, двигаться в 8 направлениях: S, N, E, W, E, NW, NE, SW, SE, записывать в журнал (кортеж или список) свой маршрут в формате coord = [x, y],
    только положительные (проверять перед шагом)"""
    def __init__(self, coord=[0, 0], age=21, sex='male'):
        super().__init__(age, sex)
        self.coord = coord

    def __str__(self):
        s = super().__str__() + f'\nHe is at {self.coord}'
        return s

class Tracer():
    """ Набор алгоритмов (в нашем случае - в глубину и ширину). Принимает сам лабиринт и искателя, ведет его по лабиринту.
    Искатель сам в это время записывает свой маршрут."""



class Trace_maker():
    """ Умеет из лабиринта и искателя построить маршрут из точек и запятых и сохранить его в файл."""