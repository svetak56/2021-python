mixed_list = [3, .423434, 'usud', (3+5j), '123', 65535, -391.31254354, None]

filtered_list = [x for x in mixed_list if x!=None]

tuple_lust = (3, 1, .32, 'wewe', -3212.3232, None, None)

dict_list = {'int': 15235, 'float': -1.3235, 'str': 'foo_cad', 'complex': (5+1.3j), 'ept':None}

filt_dict = {key: value for key, value in dict_list.items() if len(key)>3 or value!=None}

print(filt_dict)
print(filtered_list)