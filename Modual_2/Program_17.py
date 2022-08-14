a = input("Enter string one: ")
b = input("Enter string two: ")

new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]

swap_string = new_a + ' ' + new_b
print(swap_string)
