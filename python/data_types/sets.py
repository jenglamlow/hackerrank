input()
M = set([int(x) for x in input().split()])
input()
N = set([int(x) for x in input().split()])
U = M.union(N)
I = M.intersection(N)
D = sorted(U.difference(I))

for i in D:
    print(i)