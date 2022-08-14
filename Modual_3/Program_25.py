n =int(input("Enter number of tuple item with diffrent data is:"))

list = []
for i in range(n):
    x = input("Enter number only:")
    list.append(x)
print(list)
print(tuple(list))
