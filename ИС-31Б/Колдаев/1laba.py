import math

dict={'К':math.log(12),'О': math.log(16),'Л': math.log(13),'Д':math.log(5),'А':math.log(1),'Е':math.log(6),'В':math.log(3)}

print(dict['К'])
print(dict['О'])
print(dict['Л'])
print(dict['Д'])
print(dict['А'])
print(dict['Е'])
print(dict['В'])

#2


import math

d={'К':math.log(12),'О': math.log(16),'Л': math.log(13),'Д':math.log(5),'А':math.log(1),'Е':math.log(6),'В':math.log(3)}

d.items()

sorted_tuple = sorted(d.items(), key=lambda x: x[0])

dict(sorted_tuple)

print(sorted_tuple)


#3


import math

d={'К':math.log(12),'О': math.log(16),'Л': math.log(13),'Д':math.log(5),'А':math.log(1),'Е':math.log(6),'В':math.log(3)}

sorted_tuple = sorted(d.items(), key=lambda x: x[1])

dict(sorted_tuple)

print(sorted_tuple)

#4

import math

d={'К':math.log(12),'О': math.log(16),'Л': math.log(13),'Д':math.log(5),'А':math.log(1),'Е':math.log(6),'В':math.log(3)}

valuesList=list(d.values())

generator=[x for x in valuesList if x!='math.log(12)']

print(*[x for x in valuesList if x!='math.log(12)'])

#5

import math

d={'К':math.log(12),'О': math.log(16),'Л': math.log(13),'Д':math.log(5),'А':math.log(1),'Е':math.log(6),'В':math.log(3)}

valuesList=list(d.values())

sredznach=sum(valuesList)/len(valuesList)

miN=[]
maX=[]
for x in valuesList:
    if x <= sredznach:
        miN.append(x)
    else:
        maX.append(x)

print(maX)
print(miN)
