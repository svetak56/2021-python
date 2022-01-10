def f(a):
    t = 1
    while a >= 1:
        t = t * a
        a = a - 1
    return t  # факториал

# 1)словарь ключ-значение с факториалом
d = {'S': 19, 'M': 13, 'O': 15, 'L': 12, 'Y': 25, 'A': 1, 'N': 14, 'I': 9, 'N': 14, 'O': 15, 'V': 22, 'A': 1}
alf = list(d.items())
alf.sort()
otsort = dict(alf)  # 2)сортировка по ключу в афлавитном порядке(латиница)

znach = {}
znach_keys = sorted(d, key=d.get, reverse=True)  # берем значение ключа и сортируем по нему
for k in znach_keys:
    znach[k] = d[k]  # 3) от меньшего к большему


def gen():
    for i in range(1, 26):
        yield f(i)  # 4)функция-генератор для факториала


znachh = []
for i in d:
    znachh.append(d[i])  # список со значениями

n = []
v = []
sr = sum(znachh) // len(znachh)  # среднее по списку
for i in znachh:
    if i < sr:
        n.append(i)  # 5)распределение значение списка относительно его ср.знач
    elif i >= sr:
        v.append(i)
