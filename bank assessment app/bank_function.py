from ragister import Register
from dataase_connection import Database
s = Database
x = Register


class banker:

    def employeregister(self):
        Employe_id = input("enter your employe ID: ")
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

        Insert_employe = f"insert into banker values ({Employe_id}, '{Full_name}', '{Email}', '{Mobile_number}', '{Password}')"
        s.Database_Connection(s)
        s.Insert_Data(s, Insert_employe)

    def Employelogin(self):
        print("start to login procces!")
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

        Employe_login = f"select Email, Password from banker where Email='{in_Email}' AND Password='{in_Password}'"
        for _ in range(2):
            if s.Login(s, Employe_login):
                print(
                    "Enter 1 for update all customer\nEnter 2 for view all customer\nEnter 3 for delete all customer")
                num = int(input("Enter number: "))
                if num == 1:
                    s.Update_Data(s)
                elif num == 2:
                    s.viewalldata(s)
                elif num == 3:
                    print(
                        "Enter 1 for particular record deleted\nEnter 2 for all recoed delete in one cleck")
                    n = int(input("Enter above one number: "))
                    if n == 1:
                        s.Delete_Data(s)
                    elif n == 2:
                        s.Delete_Table_record(s)
                    else:
                        print("Enter valied number!")
                else:
                    print("Enter valied number!")

            else:
                print("retry to login")
