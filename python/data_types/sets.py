input()
M = set(map(int, input().split()))
input()
N = set(map(int, input().split()))
U = M.union(N)
I = M.intersection(N)
D = sorted(U.difference(I))

for i in D:
    print(i)