mylist=[]

n=int(input("Enter number of list elements:"))

for i in range(n):
    el=input("Enter the list element:")
    mylist.append(el)
print(mylist)

with open("list.txt", 'w') as f:
    for word in mylist:
        f.write(word+"\n")

fl =open("list.txt", "r")
print(fl.read())
