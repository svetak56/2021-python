# 1. Создать словарь из пар ключ-значение, где ключи - это буквы своей фамилии, а значения - это порядковый номер буквы в алфавите, от которого взят:
# a) Факториал (если вы родились весной);
# b) Число Фиббоначи (осень);
# c) Возведение в третью степень (зима);
# d) Основание натурального логарифма e^x (лето).
# 2. Отсортировать его по ключу в алфавитном порядке и сохранить в файл.
# 3. Отсортировать по значениям от меньшего к большему и сохранить в файл.
# 4. Для задания 1(а-г) написать функцию-генератор.
# 5. Создать список из значений словаря и разделить его на два: один из значений меньше среднего по списку, второй - среднее и выше.

dict = {'P': 16,'L': 12,'E': 5,'N': 14,'K': 11,'I': 9,'N': 14}

# Выводим факториалы значений библиотеки
def fact(a):    # Напишем функцию, находящую факториал числа
    if a == 0:
        return 1
    return fact(a-1) * a

dict_spring = dict.copy()   # Создадим новый словарь, где значения равны факториалу значений первого словаря
for i in dict_spring:
    dict_spring[i] = fact(dict_spring[i])


# Сортируем значения по алфовитному порядку ключей
sort1 = sorted(dict.values())
sorted_dict_1 = {}
for i in sort1:
    for k in dict.keys():
        if dict[k]==i:
            sorted_dict_1[k]= dict_spring[k]
            break

with open('sorted_1.txt','w') as out:   # Записываем отсортированный словарь в файл
    for key,val in sorted_dict_1.items():
        out.write('{}:{}\n'.format(key,val))

# Сортируем значения от меньшего к большему
sort2 = sorted(dict_spring.values())
sorted_dict_2 = {}
for i in sort2:
    for k in dict_spring.keys():
        if dict_spring[k]==i:
            sorted_dict_2[k]= dict_spring[k]
            break

with open('sorted_2.txt','w') as out:   # Записываем отсортированный словарь в файл
    for key,val in sorted_dict_2.items():
        out.write('{}:{}\n'.format(key,val))

# Списки значений меньших и больших чем среднее
values = list(dict_spring.values())
sr = sum(values) // len(values)

small_values = []
big_values = []
for i in values:
    if i < sr:
        small_values.append(i)
    elif i >= sr:
        big_values.append(i)

# Функция - генератор
dict_alphabet = {'A': 1,'B': 2,'C': 3,'D': 4,'E': 5,'F': 6,'G': 7,'H': 8,'I': 9,'J': 10,'K': 11,'L': 12,'M': 13,'N': 14,'O': 15,'P': 16,'Q': 17,'R': 18,'S': 19,'T': 20,'U': 21,'V': 22,'W': 23,'X': 24,'Y': 25,'Z': 26}
name = list(input())

dict = {}
for key in name:
    dict[key] = dict_alphabet[key]  # Не совсем правильно получилось, так как повторяющиеся буквы он выводит только один раз. Другого решения я не придумал