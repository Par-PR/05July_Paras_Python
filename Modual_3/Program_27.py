
lst = [(10,20,30),(40,50,60),(70,80,90)]
new_list= []
for tpl in lst:
    x = tpl[:-1]+(100,)
    new_list.append(x)

print(new_list)
