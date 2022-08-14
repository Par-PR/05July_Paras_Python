L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
list = []
for t in L:
    if t:
        list.append(t)
print(list)