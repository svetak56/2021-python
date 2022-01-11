#задание 1
key=['д','о','в','ы','д','е','н','к','о']
number=[5,16,3,29,5,6,15,12,16]
value=[]
for x in number:
    value.append(x**3)
a={k:v for k, v in zip(key,value)} 

#задание 2
keysort_a={k: a[k] for k in sorted(a)} 
with open('алфавитный порядок_задание2.txt', 'w') as file1:
  for key, value in keysort_a.items():
    file1.write(f'{key}, {value}\n') 

#задание 3
valuesort_a={value: a[value] for value in sorted(a)}
valuesort_a={value: key for key, value in valuesort_a.items()} 
with open('от меньшего к большему_задание3.txt', 'w') as file2:
  for key, value in valuesort_a.items():
    file2.write(f'{key}, {value}\n') 

#задание 5
big={} #для среднего и выше
small={} #для ниже среднего
middle=sum(value for value in a.values())/9 #среднее знаение
for key,value in a.items():
    if value< middle:
        small[key] = value
    else:
        big[key]=value
print('больше среднего значения',big)
print('меньше среднего значения',small)
