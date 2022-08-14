
n =int(input("Enter number of tuple item with diffrent data is:"))
list = []
for i in range(n):
    x = input("Enter number only:")
    list.append(x)

print(tuple(list))
tup = tuple(list)

def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str
 
str = convertTuple(tup)
print(str)