from itertools import combinations

N = int(input())
L = [i for i in input().strip().split(" ")]
K = int(input())

C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)
print("{0:.3}".format(len(list(F))/len(C)))