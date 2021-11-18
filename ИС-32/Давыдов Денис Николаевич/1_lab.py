import operator


def f(n):
    if n == 0:
        return 1
    return f(n-1) * n

dict = {'D': f(4), 'A': f(1), 'V': f(22), 'Y': f(25), 'O': f(15)}
print(dict)
#Первое задание

sorted_dict = sorted(dict.items())

print(sorted_dict)

file_to_save = open('Second.txt', 'w+')
file_to_save.write(str(sorted_dict))
file_to_save.close()
#Второе задание

sorted_by_value_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_by_value_dict)

file_to_save = open('Third.txt', 'w+')
file_to_save.write(str(sorted_by_value_dict))
file_to_save.close()
#Третье задание

dict_for_gen = {'D': 4, 'A': 1, 'V': 22, 'Y': 25, 'O': 15}

fun_gen = {key: f(int(value)) for key, value in dict_for_gen.items()}

print(fun_gen)
#Четвёртое задание