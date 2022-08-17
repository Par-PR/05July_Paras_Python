from turtle import width


class  Rectangle:
    lenght:float
    width :float
    def input_parameter(self):
        self.lenght = float(input("Enter lenght of rectangle: "))
        self.width = float(input("Enter width of rectangle: "))

    def area(self):
        mul = self.lenght * self.width
        print(mul)

st = Rectangle()
st.input_parameter()
st.area()
