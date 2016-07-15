import re
for i in range(int(input())):
    print("YES" if re.search(r"^[789]?", input()) is not None else "NO")