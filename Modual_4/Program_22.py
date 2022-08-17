q = "How to Define a Class in Python?"
print(q)
print()
a = "define class keyword"
print(a)
print("-------------------------")
queation = "What Is Self?"
print(queation)
print()
answer = """The self parameter is a reference to the current instance of the class,
and is used to access variables that belongs to the class."""
print(answer)
print("---------------------------")
print()

class student:
    stid = 0
    stnm = ""

    def getdata(self):
        self.stid=input("Enter Student ID:")
        self.stnm=input("Enter Student Name:")

    def printdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)

st=student()
st.getdata()
st.printdata()
