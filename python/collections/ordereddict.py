from collections import OrderedDict
d = OrderedDict()

for _ in range(int(input())):
    item, sep, n = input().rpartition(" ")
    d[item] = d.get(item, 0) + int(n)
for item, n in d.items():
    print(item, n)