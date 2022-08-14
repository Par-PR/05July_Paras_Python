from traceback import print_list


n = int(input("Enter number of element in list: "))
list = []
for i in range(n):
    x = int(input("Enter number: "))
    list.append(x)

print(list)


def large_number():
    list.sort()
    print(list[-1])

def small_number():
    list.sort()
    print(list[0])

def sum_list():
    sum = 0
    for i in range(len(list)):
        sum += list[i] 
    print(sum)


print("Large number in list is: ")
large_number()
print("small number in list is:")
small_number()
print("sum of list is:")

sum_list()