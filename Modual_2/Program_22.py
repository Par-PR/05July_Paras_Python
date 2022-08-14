def str(a):
  if len(a) < 2:
    return ''

  return a[0:2] + a[-2:]

print(str('w3resource'))
print(str('w3'))
print(str('w'))
