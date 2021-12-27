class Test():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def say_hi(self):
        print('Привет, меня зовут', self.name, '\nМне', self.age, 'лет')

f = open("E:/GitHub/2021-python/ИС-32/Давыдов Денис Николаевич/maze-for-u.txt", "r")
maze = []
for line in f:
    maze.append(line[:-1])

Jack = Test(maze, str(19), 'Male')
Jack.say_hi()