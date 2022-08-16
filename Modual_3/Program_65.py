import math
height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))
volume = math.pi * radian * radian * height
sur_area = ((2*math.pi*radian) * height) + ((math.pi*radian**2)*2)
print("Volume is: ", volume)
print("Surface Area is: ", sur_area)