def f(n):
    if n == 0:
        return 1
    return f(n-1) * n

d = {'D': f(4), 'A': f(1), 'V': f(22), 'Y': f(25), 'O': f(15)}