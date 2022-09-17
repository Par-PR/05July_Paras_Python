from customer import customer1
from bank_function import banker
b = banker
c = customer1


def customer():
    print("Enter 1 for can register account\nEnter 2 for login account")
    num = int(input("Enter number: "))
    if num == 1:
        customer1.customerregister(c)
        customer1.customerlogin(c)
    elif num == 2:
        customer1.customerlogin(c)
    else:
        print("Invalid number")


def Employe():
    print("Enter 1 for can register account\nEnter 2 for login account")
    num = int(input("Enter number: "))
    if num == 1:
        b.employeregister(b)
        b.Employelogin(b)
    elif num == 2:
        b.Employelogin(b)
    else:
        print("Invalid number")


print("who are you?")
print("Enter 1 for employe\nEnter 2 for customer")
m = int(input("Enter number for who are you: "))
if m == 1:
    Employe()
elif m == 2:
    customer()
else:
    print("Enter Valied Number")
