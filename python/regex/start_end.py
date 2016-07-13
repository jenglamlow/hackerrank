import re
S, k = input(), input()
end_pos = len(S)
i = 0
found = False
while i != end_pos:
    m = re.search(k,S[i:])
    if m:
        print((m.start()+i, m.end()+i-1))
        found = True
        i += m.start()+1
    else:
        i += 1

if not found:
    print((-1,-1))