my_list = [4, 'why', 89, 9.99, -12345128, (3 + 5j), None]

filter_l = [x for x in my_list if x!=None]

tuple_l = (3, 89, 123, 4509683.2, 'no', 1000-7, 'str', None, None)

dict_list = {'int' : 16768, 'float': -1.3273, 'str': 'foo_cad', 'complex': (5+1.3j), 'ept': None}

filt_dict = {key: value for key, value in dict_list.items() if len(key)>3 or value!= None}

print(filt_dict)
print(filter_l)