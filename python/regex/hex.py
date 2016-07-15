import re
for _ in range(int(input())):
    m = re.findall(r'(?<!^)#[a-f0-9]{3,6}', input(), flags=re.I)
    if m:
        print(*m, sep='\n')