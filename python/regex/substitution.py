import re
for i in range(int(input())):
    S = input()
    S = re.sub(r"(?<= )&&(?= )", "and", S)
    S = re.sub(r"(?<= )\|\|(?= )", "or", S)
    print(S)