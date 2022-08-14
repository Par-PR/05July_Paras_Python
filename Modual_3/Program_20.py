n =int(input("Enter number of tuple item with diffrent data is:"))
list = []
for i in range(n):
    x = input("Enter number only:")
    list.append(x)

print(tuple(list))
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)