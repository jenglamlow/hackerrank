from collections import OrderedDict

s = input()
n = int(input())

L = [list(OrderedDict.fromkeys(s[i:i+n])) for i in range(0, len(s), n)]

for s in L:
    print("".join(str(i) for i in s))