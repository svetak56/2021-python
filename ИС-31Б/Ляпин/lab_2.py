def fact(a):
  if a == 0:
    return 1
  return fact(a-1) * a

dct = {'Л': 13, 'Я': 33, 'П': 17, 'И': 10, 'Н': 15}
for i in dct:
  dct[i] = fact(dct [i])
sor_d =  sorted(dct.values())
sorted_dct = {} # 2 в алфавитном порядке
print(dct)
for i in sor_d:
  for j in dct.keys():
    if dct[j]==i:
      sorted_dct[j]= dct[j]
      break

dict1 = {} # 3 от меньшего к большему
sort_dict1 = sorted(dct, key=dct.get)
for i in sort_dict1:
  dict1[i]= dct[i]

# 5 пункт
lst = []
for i in dct:
  lst.append(dct[i])
sr = sum(lst) // len(lst)

lst1 = [] #меньше среднего
lst2 = [] #среднее и выше
for i in lst:
  if i < sr:
    lst1.append(i)
  elif i>= sr:
    lst2.append(i)