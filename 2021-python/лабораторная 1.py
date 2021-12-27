dictionary={'a': 1**3, 'n': 14**3, 'o': 15**3, 'h': 8**3, 'i': 9**3, 'n': 14**3, 'a': 1**3}
dictionary.items()
sorted_increase = sorted(dictionary.items(), key=lambda x: x[0])
dict(sorted_increase)
sorted_waning = sorted(dictionary.items(), key=lambda x: x[0], reverse=True)
dict(sorted_waning)
print(sorted_increase)
print(sorted_waning)
for key in dictionary:
    x = dictionary[key]
    y= round(pow(x,1/3),10)
print (x,y)
if y%1==0:
    print('yes')
else:
    print('no')
list1 = list(dictionary.values())
listbiger=[]
listsmaller=[]
list1 = list(dictionary.values())
srlist=sum(dictionary.values())/len(dictionary)
for x in list1:
    if x>=srlist:
        listbiger.append(x)
    else:
        listsmaller.append(x)
print(listbiger)
print(listsmaller)
