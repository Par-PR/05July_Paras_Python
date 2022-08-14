# with temp

a = 10
b = 22

print(a , end=" ")
print(b)

x = a
a = b
b = x
print(a , end=" ")
print(b)

# with out temp

l = 50
n = 83

print(l, end=" ")
print(n)

s = l + n
l = s - l
n = s - n

print(l, end=" ")
print(n)
