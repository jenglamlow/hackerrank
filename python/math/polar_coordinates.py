import cmath
z = complex(input())
print(abs(z))
print(cmath.phase(z))

# From discussion (pythonic way):
# print(*cmath.polar(complex(input())), sep='\n')