A = int(input("Ente factorial number:"))
Factorial = 1

if A < 0:
    print("Number is wrong")
elif A == 0:
    print("Factorial is one")
else:
    for i in range(1,A+1):
        Factorial = Factorial *i
print("Factorial is given number:", Factorial)
