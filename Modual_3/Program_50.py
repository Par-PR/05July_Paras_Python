k,l = input("Enter range of no.: ").split()
a = int(input("Enter check to number in range: "))

def test_range(n):
    if n in range(int(k),int(l)):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(a)
