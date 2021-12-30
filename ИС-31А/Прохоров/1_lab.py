main_list =['ff', 1, 4, 6, None, 19, 'u', 0.29493, 485, (5j + 3)]
filtered_list = [x for x in main_list if x != None]
tuple_list = (3, 1, -32, 'memes', None, None)
dict_list = {'int': 1623732, 'float': -1.3273, 'str': 'foo_cad', 'complex': (5+1.3j), 'ept': None}
filt_dict = {key: value for key, value in dict_list.items() if len(key) > 3 or value != None}
print (filt_dict)
print (filtered_list)
