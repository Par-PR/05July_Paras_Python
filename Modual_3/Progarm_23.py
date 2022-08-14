n =int(input("Enter number of tuple item with diffrent data is:"))

list = []
for i in range(n):
    x = input("Enter number only:")
    list.append(x)

print(tuple(list))
tup = tuple(list)
k = input("Enter finding string in tuple")
if k in tup:
    print("find the strint in tuple is string:", k)
else:
    print("not finding")
