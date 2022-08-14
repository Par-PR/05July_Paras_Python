tuple1 = (2, 3, 54, 6, 5, 48, 75, 145, 54, 54, 664, 25, 14, 25, 145, 25, 2, 44)
list=[]
new_list = []
for i in tuple1:
    if i in list:
        new_list.append(i)
    else:
        list.append(i)
y = tuple(list)
k = sorted(y)
print(k)

print("Repeted eliment is:", set(new_list))