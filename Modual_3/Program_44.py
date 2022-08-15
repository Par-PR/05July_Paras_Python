x = """The Python zip() function is used to contain multiple iterables together and returns them as another iterable."""

keys = ['Id', 'name', 'sub', 'fee']
values = [101, 'Paras', 'Python', 35000]

new_dict = dict(zip(keys, values))
print(new_dict)
