import re
s = input()
a = bool(re.search(r'^[1-9]\d{5}$', s))
b = len(re.findall(r'(?=(\d)\d\1)', s)) < 2
print(a and b)