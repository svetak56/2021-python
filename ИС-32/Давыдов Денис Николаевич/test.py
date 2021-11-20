def f(n):
    if n == 0:
        return 1
    return f(n - 1) * n


dict = {'D': 4, 'A': 1, 'V': 22, 'Y': 25, 'O': 15}

g = dict.values()

sred = (sum(g) / len(g))

dict_for_5_1 = [i for i in g if i < sred]
dict_for_5_2 = [i for i in g if i > sred]

print(dict_for_5_1)
print(dict_for_5_2)

