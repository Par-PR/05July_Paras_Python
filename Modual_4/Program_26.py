A = """Inheritance relationship defines the classes that inherit
from other classes as derived, subclass, or sub-type classes.
Base class remains to be the source from which a subclass inherits."""
print(A)

print("----------Example----------")
print("(1).  Single Inheritance")
class Country:
     def ShowCountry(self):
         print("This is Spain")

class State(Country):
     def ShowState(self):
         print("This is State")

st =State()
st.ShowCountry()
st.ShowState()

print("-----------------------------")
print("(2).  Multi-Level inheritance")

class Animal:  
    def speak(self):  
        print("Animal Speaking")    

class Dog(Animal):  
    def bark(self):  
        print("dog barking")  

class DogChild(Dog):  
    def eat(self):  
        print("Eating bread…")  

d = DogChild()  
d.bark()  
d.speak()  
d.eat() 

print("------------------------------")
print("(3).  Multiple Inheritance")
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  

class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  

class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  

d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))
print()
print("-----------------What is init?----------------")
l = """The Default __init__ Constructor in C++ and Java.
Constructors are used to initializing the object’s state.
The task of constructors is to initialize(assign values)
to the data members of the class when an object of the
class is created. Like methods, a constructor also contains
a collection of statements(i.e. instructions) that are
executed at the time of Object creation. It is run as
soon as an object of a class is instantiated. The method
is useful to do any initialization you want to do with your object"""
print(l)
print()
print("-------------What Is A Constructor In Python?----------------")
m = """The constructor is a method that is called when an object is created.
This method is defined in the class and can be used to initialize basic variables.
If you create four objects, the class constructor is called four times.
Every class has a constructor, but its not required to explicitly define it."""
print(m)