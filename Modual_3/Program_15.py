n =int(input("Enter number of list item is:"))
list = []
for i in range(n):
    x = input("Enter number only:")
    list.append(x)

print(list)

list.sort()
print("Second smallest number is:",list[1])
