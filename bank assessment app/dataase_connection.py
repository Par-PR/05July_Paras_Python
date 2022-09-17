import pymysql


class Database:

    dbcon = pymysql.connect(host='localhost', user='root',
                            password='', database='bankapplication')
    cur = dbcon.cursor()

    def Database_Connection(self):
        try:
            dbcon = self.dbcon
            print("Database connected...!")
        except Exception as e:
            print(e)

    def Insert_Data(self, x):

        try:
            self.cur.execute(x)
            self.dbcon.commit()
            print("Record inserted!")
        except Exception as e:
            print(e)

    def Login(self, x):

        try:
            if self.cur.execute(x):
                print("login successful")
                return True
        except Exception as e:
            print(e)
            return False

    def depositAmount(self, email, amount):
        x = f"select balence from coutomer where Email = '{email}'"
        self.cur.execute(x)
        List = list(self.cur)
        deposite = List[0][0]
        deposite += amount
        y = f"update coutomer set Balence = {deposite} where Email='{email}'"
        self.cur.execute(y)
        self.dbcon.commit()

    def withdrawAmount(self, email, amount):
        x = f"select balence from coutomer where Email = '{email}'"
        self.cur.execute(x)
        List = list(self.cur)
        deposite = List[0][0]
        if deposite >= amount:
            deposite -= amount
            y = f"update coutomer set Balence = {deposite} where Email='{email}'"
            self.cur.execute(y)
            self.dbcon.commit()
        else:
            print("enter valid amount")

    def showAmount(self, email):
        x = f"select balence from coutomer where Email = '{email}'"
        self.cur.execute(x)
        List = list(self.cur)
        deposite = List[0][0]
        print(deposite)

    def Update_Data(self):
        row = ("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'coutomer'")
        x = self.cur.execute(row)
        print(list(self.cur))
        updatevalue = input(
            "Enter column name with enter new value following data type: ")
        condition = input("Enter the email ID for update record: ")
        Update_data = f"update coutomer set {updatevalue} where Email ='{condition}'"
        try:
            self.cur.execute(Update_data)
            self.dbcon.commit()
            print("Record Updated!")
        except Exception as e:
            print(e)

    def viewalldata(self):
        x = "select * from coutomer"
        self.cur.execute(x)
        for i in self.cur:
            print(i)

    def Delete_Data(self):
        condition = input("Enter you delete the recoed Email ID: ")
        delete_data = f"delete from coutomer where Email = '{condition}'"
        try:
            self.cur.execute(delete_data)
            self.dbcon.commit()
            print("Record deleted")
        except Exception as e:
            print(e)

    def Delete_Table_record(self):
        delete_table_recored = f"truncate table coutomer"
        try:
            self.cur.execute(delete_table_recored)
            self.dbcon.commit()
            print("Table record deleted!")
        except Exception as e:
            print(e)
