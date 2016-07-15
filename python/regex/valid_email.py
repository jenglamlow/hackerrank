import re
import email.utils
for i in range(int(input())):
    s = email.utils.parseaddr(input())
    e = s[1]
    res = bool(re.match(r'^([A-Za-z0-9_-]+)@([A-Za-z]+)\.([A-Za-z]{1,3})$', e))
    if res:
        print(email.utils.formataddr(s))