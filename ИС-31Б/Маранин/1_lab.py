mixed_list=[5,.2424,'misja',(5+9j),'124',56432,-24.24142,None]


filtered_list=[x for x in mixed_list if x!= None]

tuple_list=(5,2,.24,'aboba',-23424.24,None,None)

dict_list={'int': 16768, 'float': -24.232, 'str': 'soda_luv', 'complex':(5+1.3j),'ept':None}

filt_dict={key:value for key, value in dict_list.items() if len(key)>3 or value!=None}

print(filt_dict)
print(filterd_list)
