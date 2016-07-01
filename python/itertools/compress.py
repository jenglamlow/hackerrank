from itertools import groupby
s = '1222311'
l = [(len(list(g)), int(k)) for k, g in groupby(s)]
print(" ".join(str(t) for t in l))