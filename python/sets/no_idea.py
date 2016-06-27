x, n, A, B = ([int(i) for i in input().strip().split(" ")] for _ in range(4))
A = set(A)
B = set(B)
print(sum([(i in A) - (i in B) for i in n]))