from collections import deque

class Maze():
    """ Считывание из файла, хранение, информация о содержимом клетки по координатам, информация о координатах сокровища."""
    def __init__(self, file, sod_klet, treasure_coord):
        self.file = file
        self.sod_klet = sod_klet
        self.treasure_coord = treasure_coord
    def open_file(self):
        self.file = open("E:/GitHub/2021-python/ИС-32/Давыдов Денис Николаевич/maze-for-u.txt", "r")

maze = []
for line in file:
    maze.append(line[:-1])
print(maze)
class Pathfinder():
    """ Информация о личности, двигаться в 8 направлениях: S, N, E, W, E, NW, NE, SW, SE, записывать в журнал (кортеж или список) свой маршрут в формате coord = [x, y],
    только положительные (проверять перед шагом)"""

class Tracer():
    """ Набор алгоритмов (в нашем случае - в глубину и ширину). Принимает сам лабиринт и искателя, ведет его по лабиринту.
    Искатель сам в это время записывает свой маршрут."""

class Trace_maker():
    """ Умеет из лабиринта и искателя построить маршрут из точек и запятых и сохранить его в файл."""