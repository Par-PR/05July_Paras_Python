def list1():
    n =int(input("Enter number of list item is:"))
    list2 = []
    for i in range(n):
        x = input("Enter list item:")
        list2.append(x)

    return list2

k = list1()
print("Enter sublist in find in main list:")
y = list1()

print("The original list : " + str(k))
print("The sublist list : " + str(y))

res = False
for idx in range(len(k) - len(y) + 1):
        if k[idx : idx + len(y)] == y:
            res = True
            break
         

print("Is sublist present in list ? : " + str(res))