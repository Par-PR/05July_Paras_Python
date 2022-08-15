import operator

mydict={}

n=int(input("Enter the number of pairs:"))

for i in range(n):
    key=input("Enter the key:")
    value=input("Enter the value:")
    mydict[key]=value

print(mydict)

s= sorted(mydict.items(), key=operator.itemgetter(1))

print('ascending order : ',s)

s1= dict( sorted(mydict.items(), key=operator.itemgetter(1),reverse=True))

print('descending order : ',s1)