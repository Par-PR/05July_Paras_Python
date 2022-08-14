n =int(input("Enter number of list item is:"))
list = []
for i in range(n):
    x = input("Enter list item:")
    list.append(x)

print(list)
sum = list
def same_string(sum):
    count = 0
    for i in sum:
        if len(i)> 1 and i[0] == i[-1]:
                count += 1
    return count

print(same_string(sum))
