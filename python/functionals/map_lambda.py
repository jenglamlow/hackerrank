f = lambda a: a if a < 2 else f(a-1) + f(a-2)
print([f(x)**3 for x in range(int(input()))])