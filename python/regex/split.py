import re
L = [x for x in re.split("[,.]?", input()) if x]
print(*L, sep="\n")
