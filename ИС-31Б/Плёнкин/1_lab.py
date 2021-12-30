mixed_list = [3, -42345, (3+5j),"eras", '173', 65535, -391, None]

filtered_list = [x for x in mixed_list if x is x!= None]

tuple_list = (3, 1, .32, "no", None, None)

dict_list = {'int': 132, 'float': -1.3232, 'str': "foo_cad", 'complex': (1+1.3j), 'ept': None}

filt_dict = {key: value for key, value in dict_list.items() if len(key)>3 if value != None}

print(filt_dict)
print(filtered_list)