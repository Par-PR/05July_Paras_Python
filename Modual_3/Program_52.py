
k = input("Enter string to check is Palindrome or not: ")

def Palindrome(string):
	Left_side = 0
	Right_side = len(string) - 1
	
	while Right_side >= Left_side:
		if not string[Left_side] == string[Right_side]:
			return False
		Left_side += 1
		Right_side -= 1
	return True
print(Palindrome(k)) 


