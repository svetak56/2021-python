import operator

#выполнение первого задания
##создаем функцию-генератор(задание 4)
def i(n):
    if n == 0:
        return 1
    yield n ** 3

SecondName = dict(R = next(i(18)), u = next(i(21)), d = next(i(4)), e = next(i(5)), n = next(i(14)), k = next(i(11)), o = next(i(15)))
print(SecondName)

#выполняем задание 2
sorted_alphavit = sorted(SecondName, key=SecondName.get)

print(sorted_alphavit)

file_to_save = open('F2.txt', 'w+')
file_to_save.write(str(sorted_alphavit))
file_to_save.close()

#выполняем задание 3
sorted_min_max = sorted(SecondName.items(), key=operator.itemgetter(1))

print(sorted_min_max)

file_to_save = open('F3.txt', 'w+')
file_to_save.write(str(sorted_min_max))
file_to_save.close()

#выполняем задание 5,
sum_dict = sum(SecondName.values())
avg_dict = sum_dict/len(SecondName.values())
o = [int(avg_dict)]
a = list(SecondName.values())
b = []
c = []
n = 1
for n in range(len(SecondName.values())):
    if a[n] < o[0]:
        b.append(a[n])
    else :
        c.append(a[n])

print(b)
print(c)
