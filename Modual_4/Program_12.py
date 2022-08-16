fl = open("test.txt", "r")
f = open("write.txt", "w")
for line in fl:
    f.write(line)