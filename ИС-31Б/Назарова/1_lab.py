#Создать словарь из пар ключ-значение, где ключи - это буквы своей фамилии, а значения - это порядковый номер буквы в алфавите, от которого взят: факториал
dict = {'н': 15,'а': 1,'з': 9,'а': 1,'р':18,'о':16,'в':2,'а':1}
def fact(a):
    if a == 0:
        return 1
    return fact(a-1) * a
for i in dict:
    dict[i] = fact(dict[i])
print(dict)

#Отсортировать его по ключу в алфавитном порядке и сохранить в файл.
sorteddict =  sorted(dict.values())
sorted_dict = {}
for i in sorteddict:
  for j in dict.keys():
    if dict[j]==i:
      sorted_dict[j]= dict[j]
      break
print(sorteddict)
file_to_save = open('file1.txt', 'w+')
file_to_save.write(str(sorted_dict[j]))
file_to_save.close()

#Отсортировать по значениям от меньшего к большему и сохранить в файл.
dict1 = {}
sorteddict1 = sorted(dict, key=dict.get)
for i in sorteddict1:
  dict1[i]= dict[i]
print(dict1)
file_to_save = open('file2.txt', 'w+')
file_to_save.write(str(sorteddict1))
file_to_save.close()

#Создать список из значений словаря и разделить его на два: один из значений меньше среднего по списку, второй - среднее и выше
dict2 = {'н': 15,'а': 1,'з': 9,'а': 1,'р':18,'о':16,'в':2,'а':1}
a = dict2.values()
mean = (sum(a) / len(a))
dict_small = [i for i in a if i < mean]
dict_big = [i for i in a if i > mean]
print('меньше среднего:', dict_small)
print('больше среднего:', dict_big)