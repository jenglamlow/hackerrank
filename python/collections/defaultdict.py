from collections import defaultdict

d = defaultdict(list)
n, m = [int(x) for x in input().split()]

for i in range(n+m):
    if i < n:
        d[input()].append(i+1)
    else:
        G = input()
        print(" ".join(str(i) for i in d[G]) if G in d else -1)

