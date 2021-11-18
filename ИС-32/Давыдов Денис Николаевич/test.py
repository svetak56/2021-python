def f(n):
    if n == 0:
        return 1
    return f(n - 1) * n


dict = {'D': 4, 'A': 1, 'V': 22, 'Y': 25, 'O': 15}

data = ()

fun_gen = {key: f(int(value)) for key, value in dict.items()}

print(fun_gen)