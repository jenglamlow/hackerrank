import re
import email.utils
for i in range(int(input())):
    s = email.utils.parseaddr(input())
    e = s[1]
    res = bool(re.match(r'^[a-zA-Z][a-zA-Z0-9-\._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', e))
    if res:
        print(email.utils.formataddr(s))