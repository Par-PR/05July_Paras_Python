fl = open("test.txt", "r")
n = int(input("Enter the you can read line: "))
for i in range(1,n+1):
    print(fl.readline())
