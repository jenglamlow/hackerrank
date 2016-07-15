import re
for _ in range(int(input())):
    s = input()
    check = True
    check = check and bool(re.match(r'[A-Za-z0-9]{10}', s))
    check = check and bool(re.match(r'(?=(.*[0-9]){3,})(.*[A-Z]){2,}', s))
    check = check and bool(re.match(r'^(?:(.)(?!.*\1)){10}$', s))
    print("Valid" if check else "Invalid")