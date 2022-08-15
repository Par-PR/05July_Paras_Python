mydict={}
n=int(input("Enter the number of pairs:"))
for i in range(n):
    key=input("Enter the key:")
    value=input("Enter the value:")
    mydict[key]=value
print(mydict)

key = input("Enter finding key in mydict:")

def check(mydict, key):
     
    if key in mydict.keys():
        print("Present, ", end =" ")
        print("value =", mydict[key])
    else:
        print("Not present")
 

check(mydict, key)