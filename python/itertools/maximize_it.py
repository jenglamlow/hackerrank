from itertools import product

N, M = map(int, input().strip().split())
L = []
for _ in range(N):
    L.append(list([int(i) for i in input().strip().split()])[1:])

P =list(product(*L))
Max = 0
for i in P:
    A = sum(map(lambda x: x*x, i)) % M
    if A > Max:
        Max = A

print(Max)
