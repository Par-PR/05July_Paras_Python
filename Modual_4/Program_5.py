n = int(input("Enter no. of print last n line: "))


f = open('test.txt',"r")
for line in (f.readlines() [-n:]):
    print(line)
