# 1


import math

dict={'М':math.log(14),'А': math.log(1),'Р': math.log(18),'А':math.log(1),'Н':math.log(15),'И':math.log(10),'Н':math.log(15)}

print(dict['М'])
print(dict['А'])
print(dict['Р'])
print(dict['А'])
print(dict['Н'])
print(dict['И'])
print(dict['Н'])

#2


import math

d={'М':math.log(14),'А': math.log(1),'Р': math.log(18),'А':math.log(1),'Н':math.log(15),'И':math.log(10),'Н':math.log(15)}

d.items()

sorted_tuple = sorted(d.items(), key=lambda x: x[0])

dict(sorted_tuple)

print(sorted_tuple)


#3


import math

d={'М':math.log(14),'А': math.log(1),'Р': math.log(18),'А':math.log(1),'Н':math.log(15),'И':math.log(10),'Н':math.log(15)}

sorted_tuple = sorted(d.items(), key=lambda x: x[1])

dict(sorted_tuple)

print(sorted_tuple)

#4

import math

d={'М': 'math.log(14)','А': 'math.log(1)','Р': 'math.log(18)','А':'math.log(1)','Н':'math.log(15)','И':'math.log(10)','Н':'math.log(15)'}

valuesList=list(d.values())

generator=[x for x in valuesList if x!='math.log(14)']

print(*[x for x in valuesList if x!='math.log(14)'])

#5

import math

d={'М': math.log(14),'А': math.log(1),'Р': math.log(18),'А':math.log(1),'Н':math.log(15),'И':math.log(10),'Н':math.log(15)}

valuesList=list(d.values())

sr_znach=sum(valuesList)/len(valuesList)

menshe=[]
bolshe=[]
for x in valuesList:
    if x <= sr_znach:
        menshe.append(x)
    else:
        bolshe.append(x)

print(bolshe)
print(menshe)
        
        






        
