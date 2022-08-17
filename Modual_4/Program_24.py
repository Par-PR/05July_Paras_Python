import math

class Circle:
    radius : float
    
    def input_parameter(self):
        self.radius = float(input("Enter radius of circle: "))
    

    def area(self):
        mul = math.pi * self.radius**2
        print(mul)

    def perimeter(self):
        total = 2 * math.pi * self.radius
        print(total)

st = Circle()
st.input_parameter()
st.area()
st.perimeter()
