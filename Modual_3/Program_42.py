dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}
print(dict1)
 
for key in dict1:
    if key in dict2:
        dict1[key] = dict1[key] + dict2[key]
    else:
        pass
res = dict2 | dict1
print(res)
