
from ragister import Register
from dataase_connection import Database
s = Database
x = Register


class customer1:

    def customerregister(self):
        Account_Number = int(input("enter your account number: "))
        Full_name = input("Enter your full name: ")
        Email = input("Enter your email id:")
        if (x.Email(x, Email)):
            pass
        else:
            print("Invalid Email!")
        Mobile_number = input("Enter your mobile number: ")
        if (x.MobileNummber(x, Mobile_number)):
            pass
        else:
            print("Invalid mobile number!")

        Password = input("enter password: ")
        if (x.Password(x, Password)):
            pass
        else:
            print("Invalid Password")
        Comfirm_password = input("Comfarm password: ")
        if Password == Comfirm_password:
            pass
        else:
            print("Password not match!")

        Belance = int(input("add some balance in your account: "))

        Insert_customer = f"insert into coutomer values ({Account_Number}, '{Full_name}', '{Email}', '{Mobile_number}', '{Password}', {Belance})"
        s.Database_Connection(s)
        s.Insert_Data(s, Insert_customer)

    def customerlogin(self):
        in_Email = input("Enter your email id:")
        if (x.Email(x, in_Email)):
            pass
        else:
            print("Invalid Email!")
        in_Password = input("enter password: ")
        if (x.Password(x, in_Password)):
            pass
        else:
            print("Invalid Password")

        customer_login = f"SELECT * FROM coutomer WHERE Email='{in_Email}' AND Password='{in_Password}'"
        for _ in range(2):
            if s.Login(s, customer_login):
                print(
                    "Enter 1 for deposite amount\nenter 2 for widroha amounr\nEnter 3 for view amount")
                num = int(input("Enter number: "))
                if num == 1:
                    n = int(input("Ente amount: "))
                    s.depositAmount(s, in_Email, n)
                elif num == 2:
                    l = int(input("Enter amount: "))
                    s.withdrawAmount(s, in_Email, l)
                elif num == 3:
                    s.showAmount(s, in_Email)
                else:
                    print("Enter Valied Number!")

            else:
                print("retry to login")
