
x = """
Try:-     This block will test the excepted error to occur
Except:-  Here you can handle the error
Else:-    If there is no exception then this block will be executed
Finally:- Finally block always gets executed either exception is generated or not"""
print(x)


try:
	k = 5/0
	print(k)

except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	print('This is always executed')
