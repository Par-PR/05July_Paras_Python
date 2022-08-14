n =int(input("Enter number of list item is:"))
list = []
for i in range(n):
    x = input("Enter list item:")
    list.append(x)

print(list)

list1 = set(list)
print(list1)