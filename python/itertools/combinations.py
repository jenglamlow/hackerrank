from itertools import combinations
s, n = input().split(" ")
for j in range(1, int(n)+1):
    for i in list(combinations(sorted(s),j)):
        print("".join(i))