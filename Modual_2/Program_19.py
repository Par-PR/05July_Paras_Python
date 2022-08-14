str1 = input("enter string: ")
A = str1.find('not')
B = str1.find('poor')
  

if B > A and A>0 and B>0:
  str1 = str1.replace(str1[A:(B+4)], 'good')
  print(str1)
else:
  print(str1)
  