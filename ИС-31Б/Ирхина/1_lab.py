
dict = {'I': 9,'R': 18,'H': 8,'I': 9,'N': 14,'A': 1}


#1
def fact(a):
    if a == 0:
        return 1
    return fact(a-1) * a

dict_spring = dict.copy()
for i in dict_spring:
    dict_spring[i] = fact(dict_spring[i])
print(dict_spring)


#2
sort1 = sorted(dict.values())
sorted_1 = {}
for i in sort1:
    for k in dict.keys():
        if dict[k]==i:
            sorted_1[k]= dict_spring[k]
            break
print(sorted_1)     #Результат

with open('sorted_1.txt','w') as out:     #Запись в файл
    for key,val in sorted_1.items():
        out.write('{}:{}\n'.format(key,val))


#3
sort2 = sorted(dict_spring.values())
sorted_2 = {}
for i in sort2:
    for k in dict_spring.keys():
        if dict_spring[k]==i:
            sorted_2[k]= dict_spring[k]
            break
print(sorted_2)     #Результат

with open('sorted_2.txt','w') as out:     #Запись в файл
    for key,val in sorted_2.items():
        out.write('{}:{}\n'.format(key,val))


#5
values = list(dict_spring.values())
sr = sum(values) // len(values)

small_values = []
big_values = []
for i in values:
    if i < sr:
        small_values.append(i)
    elif i >= sr:
        big_values.append(i)

