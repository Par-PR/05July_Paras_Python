
def dict1():
    mydict={}
    n=int(input("Enter the number of pairs:"))

    for i in range(n):
        key=input("Enter the key:")
        value=input("Enter the value:")
        mydict[key]=value
    return mydict

d1 = dict1()
d2 = dict1()
x = {}
for i in (d1, d2):
    x.update(i)

print(x)