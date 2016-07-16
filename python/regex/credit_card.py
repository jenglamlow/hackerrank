import re
for i in range(int(input())):
    check = bool(re.match(r'^(?=^[456])(?!.*(\d)(?:-?\1){3,})(?:\d{4}\-?){4}$', input()))
    print("Valid" if check else "Invalid")