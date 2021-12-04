import math
List = {"м":math.log(15) ,"а":math.log(1) , "л":math.log(14) ,"ы":math.log(30) ,"ш":math.log(27) ,"е":math.log(6) ,"в":math.log(3)}

list_sort_keys = list(List.keys()) #создаем список ключей словаря
list_sort_keys.sort() # сотируем по ключам алфавита

list_sort_items = list(List.items()) #создаем список значений словаря
list_sort_items.sort(key=lambda i: i[1]) # сортируем от меньшего к большему







five_list = (i[1] for i in List.items()) # создаем список с значениями из словаря

mean_five_list = sum(List.values()) / len(List) # находим среднее значение 


five_list_max =  (x for x in five_list if x >= mean_five_list)  # записываем в переменную числа из списка больше среднего
five_list_min =  (x for x in five_list if x < mean_five_list ) # записываем в переменную числа из списка меньше среднего


