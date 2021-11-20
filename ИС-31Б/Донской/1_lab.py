def fact(a):
  if a == 0:
    return 1 
  return fact(a-1) * a

dct = {'Д': 5, 'О': 16, 'Н': 15, 'С': 19, 'К': 12, 'О':16, 'Й': 11, }
for i in dct:
  dct[i] = fact(dct [i])
sor_d =  sorted(dct.values())

# 2

sorted_dct = {} 
print(dct)
for i in sor_d:
  for j in dct.keys():
    if dct[j]==i:
      sorted_dct[j]= dct[j]
      break

# 3

dict1 = {}  
sort_dict1 = sorted(dct, key=dct.get)
for i in sort_dict1:
  dict1[i]= dct[i]

# 4

import math

d={'Д': 'math.log(5)','О': 'math.log(16)','Н': 'math.log(15)','С':'math.log(19)','К':'math.log(12)','О':'math.log(16)','Й':'math.log(11)'}

valuesList=list(d.values())

generator=[x for x in valuesList if x!='math.log(14)']

print(*[x for x in valuesList if x!='math.log(14)'])

# 5 

lst = []
for i in dct:
  lst.append(dct[i])
sr = sum(lst) // len(lst)

lst1 = [] 
lst2 = [] 
for i in lst:
  if i < sr: 
    lst1.append(i)
  elif i>= sr:
    lst2.append(i)