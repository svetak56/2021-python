import operator

# Первое задание


def f(n):
    return n**3


diction = {'O': f(15), 'S': f(19), 'M': f(13), 'I': f(6), 'N': f(14)}
print(diction)

# Второе задание

sorted_by_letter_diction = sorted(diction.items())

print(sorted_by_letter_diction)

save_to = open('Second.txt', 'w+')
save_to.write(str(sorted_by_letter_diction))
save_to.close()

# Третье задание

sorted_by_value_diction = sorted(diction.items(), key=operator.itemgetter(0), reverse=True)

print(sorted_by_value_diction)

save_to = open('Third.txt', 'w+')
save_to.write(str(sorted_by_value_diction))
save_to.close()

# Четвертое задание

gen_diction = {'O': 15, 'S': 19, 'M': 13, 'I': 6, 'N': 14}

genf = {key: f(int(value)) for key, value in gen_diction.items()}
 
print(genf)


def genfactorial(x):
    y = 1
    for i in range(x):
        if i in (0, 1):
            yield 1
        else:
            y = y*i
            yield y


for i in genfactorial(12):
    print(i)

# Пятое задание

diction_mean = {'O': 15, 'S': 19, 'M': 13, 'I': 6, 'N': 14}

a = diction_mean.values()

mean = (sum(a) / len(a))  # среднее арифметическое

diction_mean_smaller = [i for i in a if i < mean]
diction_mean_bigger = [i for i in a if i > mean]

print('значения меньше среднего:', diction_mean_smaller)
print('значения больше среднего:', diction_mean_bigger)


