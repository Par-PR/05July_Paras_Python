L = [{"V":"1001"}, {"V": "1002"}, {"VI": "1001"}, {"VI": "1005"}, {"VII":"1005"}, {"V":"1009"},{"VIII":"1007"}]
s = set()
for dic in L:
   for val in dic.values():
      s.add(val)

print("Unique Values: ",s)
