try:
    num = int(input("Enter a number: "))
    assert num % 2 != 0
    print("number is odd")
except:
    print("Error: ",end="")
    print("Number is an even!")
