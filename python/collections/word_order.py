from collections import OrderedDict
d = OrderedDict()

for _ in range(int(input())):
    word = input()
    d[word] = d.get(word, 0) + 1

print(len(d))
print(" ".join(str(count) for word, count in d.items()))