from datetime import datetime
for _ in range(int(input())):
    t0 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    t1 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    diff = t1-t0
    print(int(abs(diff.total_seconds())))