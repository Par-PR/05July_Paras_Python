from myfunction import Database
x = Database
Database.Database_Connection(x)
print("Enter 1 for create table\nEnter 2 for inserte record\nEnter 3 for update record\nEnter 4 for delete record\nEnter 5 for delete table\nEnter 6 for delete table all record\nEnter 7 for show data from table")
n = int(input("Enter above number to comlete your opretion: "))

if n == 1:
    Database.Create_Table(x)
elif n == 2:
    Database.Insert_Data(x)
elif n == 3:
    Database.Update_Data(x)
elif n == 4:
    Database.Delete_Data(x)
elif n == 5:
    Database.Delete_Table(x)
elif n == 6:
    Database.Delete_Table_record(x)
elif n == 7:
    Database.Show_Data(x)
else:
    print("invalied oparetion number pleas enter valied opration number")
