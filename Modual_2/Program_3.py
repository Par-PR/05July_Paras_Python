x = int(input("Enter Fibonacci series range number:"))
n1 = 0
n2 = 1


if x <= 0:
    print("given number is wronge")
elif x == 1:
    print(n1)
else:
    print(n1)
    for i in range(2,x+1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n1)
