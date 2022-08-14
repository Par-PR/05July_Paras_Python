def insert(str):
    mid = len(str)//2
    return str[:mid] + '-' + str[mid:]

print(insert("parashpethani"))