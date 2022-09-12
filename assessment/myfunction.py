import pymysql


class Database:

    dbcon = pymysql.connect(host='localhost', user='root',
                            password='', database='paras')
    cur = dbcon.cursor()

    # Data Connection
    def Database_Connection(self):
        try:
            dbcon = self.dbcon
            print("Database connected...!")
        except Exception as e:
            print(e)

        self.cur.execute("select database()")
        db_name = self.cur.fetchone()[0]
        print("Your database name: ", db_name)

    # Table Create
    def Create_Table(self):
        TableName = input("enter tablename: ")
        column = input("enter columns and column atrribute: ")
        tbl_create = "create table {0}({1})".format(TableName, column)
        try:
            self.cur.execute(tbl_create)
            print("Table created!")
        except Exception as e:

            print(e)

    # Insert Data
    def Insert_Data(self):
        Table_name = self.cur.execute("SHOW TABLES")
        print("This database in number of table is :", Table_name)
        print("Table name is:", list(self.cur))
        TableName1 = input("Enter above table name: ")
        row = (
            f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{TableName1}'")
        x = self.cur.execute(row)
        print(list(self.cur))
        n = input("Enter the record in table for follwing colemn index and added the maltipale record useing the formet is like: (integer, 'text','text'), :\n\t")
        insert_data = f"insert into {TableName1} values {n}"
        try:
            self.cur.execute(insert_data)
            self.dbcon.commit()
            print("Record inserted!")
        except Exception as e:
            print(e)

    # Update Data
    def Update_Data(self):
        Table_name = self.cur.execute("SHOW TABLES")
        print("This database in number of table is :", Table_name)
        print("Table name is:", list(self.cur))
        TableName = input("Enter above table name: ")
        row = (
            f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{TableName}'")
        x = self.cur.execute(row)
        print(list(self.cur))
        updatevalue = input(
            "Enter column name with enter new value following data type ")
        condition = input(
            "Enter column information show and write condition to delete record: ")
        Update_data = f"update {TableName} set {updatevalue} where {condition}"
        try:
            self.cur.execute(Update_data)
            self.dbcon.commit()
            print("Record Updated!")
        except Exception as e:
            print(e)

    # Delete Data
    def Delete_Data(self):
        Table_name = self.cur.execute("SHOW TABLES")
        print("This database in number of table is :", Table_name)
        print("Table name is:", list(self.cur))
        Tablename = input("Enter above table name for delete table record: ")
        row = (
            f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{Tablename}'")
        x = self.cur.execute(row)
        print(list(self.cur))
        condition = input(
            "Enter column information show and write condition to delete record: ")
        delete_data = f"delete from {Tablename} where {condition}"
        try:
            self.cur.execute(delete_data)
            self.dbcon.commit()
            print("Record deleted")
        except Exception as e:
            print(e)

    # Delete Table
    def Delete_Table(self):
        Table_name = self.cur.execute("SHOW TABLES")
        print("This database in number of table is :", Table_name)
        print("Table name is:", list(self.cur))
        Tablename = input("Enter above table name for delete table record: ")
        delete_table = f"drop table {Tablename}"
        try:
            self.cur.execute(delete_table)
            self.dbcon.commit()
            print("Table deleted!")
        except Exception as e:
            print(e)

    # Delete Table Recored
    def Delete_Table_record(self):
        Table_name = self.cur.execute("SHOW TABLES")
        print("This database in number of table is :", Table_name)
        print("Table name is:", list(self.cur))
        Tablename = input("Enter above table name for delete table record: ")
        delete_table_recored = f"truncate table {Tablename}"
        try:
            self.cur.execute(delete_table_recored)
            self.dbcon.commit()
            print("Table record deleted!")
        except Exception as e:
            print(e)

        # Show Data
    def Show_Data(self):
        Table_name = self.cur.execute("SHOW TABLES")
        print("This database in number of table is :", Table_name)
        print("Table name is:", list(self.cur))
        Tablename = input("Enter above table name for delete table record: ")
        select_data = f"select * from {Tablename}"
        try:
            self.cur.execute(select_data)
            print(
                "Enter 1 to show all data\nEnter 2 for show many data\nEnter 3 for only show the first row")
            l = int(input("Enter the above nomber: "))
            if l == 1:
                data = self.cur.fetchall()
            elif l == 2:
                s = int(input("Enter number to show the number of row data: "))
                data = self.cur.fetchmany(s)
            elif l == 3:
                data = self.cur.fetchone()
            else:
                print("Invalid Number!")
            print(data)
        except Exception as e:
            print(e)
