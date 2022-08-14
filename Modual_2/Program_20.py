def long_word(wordslist):
    word_len = []
    for n in wordslist:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0]
result = long_word(["PHP", "Exercises", "Backend"])
print("Length of the longest word:",result)
