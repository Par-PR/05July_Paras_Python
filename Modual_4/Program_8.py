f = open("text.txt", 'r')
l = f.read().split()
max_len = len(max(l, key=len))

for word in l:
    if len(word) == max_len:
        print(word)
