def fact(a):
  if a == 0:
    return 1 
  return fact(a-1) * a
#1
dict1 = {'К': 12, 'Р': 18, 'У': 21, 'Г': 4, 'Л': 13, 'О':16, 'В': 3, 'А': 1}
for b in dict1:
  dict1[b] = fact(dct [b])
sor_d =  sorted(dict1.values())
sorted_dict1 = {} #2
print(dict1)
for b in sor_d:
  for c in dict1.keys():
    if dict1[c]==b:
      sorted_dict1[c]= dict1[c]
      break
#3
dict2 = {} 
sort_dict2 = sorted(dict1, key=dict1.get)
for b in sort_dict2:
  dict2[b]= dict1[b]

# 5 
lst = []
for b in dict1:
  lst.append(dict1[i])
sr = sum(lst) // len(lst)

lst1 = [] 
lst2 = [] 
for b in lst:
  if b < sr: 
    lst1.append(b)
  elif b>= sr:
    lst2.append(b) 
