def list1():
    n =int(input("Enter number of list item is:"))
    list2 = []
    for i in range(n):
        x = input("Enter list2 item:")
        list2.append(x)

    return list2

k = list1()

y = list1()

def common_member(k, y):
    result = False
    for a in k:
        for b in y:
            if a == b:
                result = True
    return result


print(common_member(k, y))

