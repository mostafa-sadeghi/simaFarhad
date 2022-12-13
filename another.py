chars = ['a', 'b', 'c', 'd']

del chars[1]
print(chars)

chars.remove('d')
print(chars)

chars.pop()
chars = ['a', 'b', 'c', 'd']
ch = chars.pop(1)
print(ch)
print(chars)
