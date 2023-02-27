a = 1
b = 2
c = 3
print(a, b, c, end='\n')
a, b = b, a
print(a, b, c, end='\n')
b, c = c, b
print(a, b, c, end='\n')
