
x = """Memory in Python is managed by Python private heap space.
All Python objects and data structures are located in a private heap.
This private heap is taken care of by Python Interpreter itself, and a programmer does not have access to this private heap.
Python memory manager takes care of the allocation of Python private heap space.
Memory for Python private heap space is made available by Python is in-built garbage collector,
which recycles and frees up all the unused memory."""
print(x)
#static memory allocation
a = 20
b = [] 
c = "" 
print(a)
print(b)
print(c)

#dynamic memory allocation

y = [0]*5  #This memory for 5 integers is allocated on heap.  

print(y)

#garbage collector

class Test(object):
    pass

z = Test()
z.obj = z
del z
