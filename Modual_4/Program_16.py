Question = "Can one block of except statements handle multiple exception?"

Answer = """yes, like except TypeError, SyntaxError [,. . . ]
        Each type of exception can be specified directly.
        There is no need to put it in a list."""

print(Question)
print()
print(Answer)
