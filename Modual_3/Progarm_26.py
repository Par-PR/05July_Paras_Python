n =int(input("Enter number of tuple item with diffrent data is:"))

list = []
for i in range(n):
    x = input("Enter number only:")
    list.append(x)

tup = tuple(list)
print("The original tuple is:", tup)
y = tuple(reversed(tup))
print("The reversed tuple is:",y)
