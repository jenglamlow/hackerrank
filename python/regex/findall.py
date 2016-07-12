import re
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r'(?<=[%s])([aeiou]{2,})(?=[%s])' % (c, c) , input(), flags=re.I)
print('\n'.join(m or ['-1']))