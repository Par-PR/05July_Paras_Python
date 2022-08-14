def reverse_string(str1):
    x = ""
    if len(str1) % 4 == 0:
       return x.join(reversed(str1))
    return str1

print(reverse_string('abcd'))
print(reverse_string('python'))
