import re
N,M = map(int, input().split())
L = []
for i in range(N):
    L.append(input())

S = "".join(["".join(c) for c in zip(*L)])
S = " ".join(re.split(r'\b[^a-zA-Z0-9]*\b', S))
print(S)