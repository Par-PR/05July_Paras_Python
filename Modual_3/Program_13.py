n =int(input("Enter number of list item is:"))
list = []
for i in range(n):
    x = input("Enter string element item:")
    list.append(x)

print(list)

string = ''.join(list)
print(string)