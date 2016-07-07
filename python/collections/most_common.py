from collections import Counter, OrderedDict

C = Counter(input())
od = OrderedDict(sorted(C.items(), key=lambda k:(-k[1], k[0])))
count = 0
for k, v in od.items():
    if count == 3:
        break
    print(k,v)
    count += 1
