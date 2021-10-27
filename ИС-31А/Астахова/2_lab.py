def fact(a):
  if a == 0:
    return 1 
  return fact(a-1) * a

dct = {'A': 1, 'С': 19, 'Т': 20, 'А': 1, 'Х': 23, 'О':16, 'В': 3, 'А': 1}
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
lst2 = [] #больше и равное среднего
for i in lst:
  if i < sr: 
    lst1.append(i)
  elif i>= sr:
    lst2.append(i)