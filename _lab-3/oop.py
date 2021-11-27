class Man():
    def __init__(self, age=21, sex='male', is_blind=False):
        self.age = age
        self.sex = sex
        self.is_blind = is_blind

    def __str__(self):
        return f'The {self.sex} person, age {self.age} is {self.is_blind} blind'

    def set_age(self, age):
        self.age = age
    def get_age(self):
        return self.age

    def set_sex(self, sex):
        if sex in ('male', 'female'):
            self.sex = sex
    def get_sex(self):
        return self.sex

    def set_is_blind(self, is_blind):
        self.is_blind = True if is_blind else False
    def get_is_blind(self):
        return self.is_blind

class Pathfinder(Man):
    """
    Двигаться в 8 направлениях: S, N, E, W, E, NW, NE, SW, SE
    Записывать в журнал (кортеж или список) свой маршрут
    формат coord = [x, y], только положительные (проверять перед шагом)
    """
    def __init__(self, coord=[0, 0], is_rich=False, age=21, sex='male', is_blind=False):
        super().__init__(age, sex, is_blind)
        self.coord = coord
        self.is_rich = is_rich
    def __str__(self):
        s = super().__str__() +f'\nHe is at {self.coord}'
        s += ' and VERY rich!' if self.is_rich else ' and poor as mouse.'
        return s


john = Pathfinder(age=49, coord=[5, 3], is_rich=True)
print(john)
pete = Man(age=14, sex='female', is_blind=True)
print(pete)