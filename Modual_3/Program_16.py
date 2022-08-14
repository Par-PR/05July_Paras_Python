n =int(input("Enter number of list item is:"))
l = []
for i in range(n):
    x = input("Enter list item:")
    l.append(x)

print(l)

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list(l)) 
