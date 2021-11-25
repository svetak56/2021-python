import math

def fun(x):
    if (x == 0):
        return 1
    #y = 1
    #z = 1
    #while(x != (y-1)):
     #   z *= y
      #  y += 1
    #return z
    return fun(x-1) * x

#4?
def gen(x):
    if x is 0:
        yield 1
    else:
        y = 1
        for i in range(x) + 1:
            y = y * i
            yield y * (i-1)
        

#1
list1 = {'Ч':25, 'Е':6, 'Р':18, 'В':3, 'Я':33, 'К':12, 'О':16, 'В':3}

for i in list1:
    list1[i] = fun(list1[i])
print(list1)

#2
sorted_l = sorted(list1.values())
sorted_l2 = {}
for i in sorted_l:
    for j in list1.keys():
        if list1[j] == i:
            sorted_l2[j] = list1[j]
print(sorted_l2)

#3?
list2 = sorted(list1)
print(list2)
list3 = sorted(list1.values())
print(list3)

#5
sr_znach = sum(list3) / len(list3)

listabove = []
for i in list3:
    if i > sr_znach:
        listabove.append(i)
print(listabove)

listlower = []
for i in list3:
    if i < sr_znach:
        listlower.append(i)
print(listlower)