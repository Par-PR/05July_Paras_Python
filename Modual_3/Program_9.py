n =int(input("Enter number of list item is:"))
list = []
for i in range(n):
    x = input("Enter list item:")
    list.append(x)

print(list)

if list:
    print("list is not empty")
else:
    print("list is empty")