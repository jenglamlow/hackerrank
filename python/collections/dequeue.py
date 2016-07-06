from collections import deque

d = deque()
for _ in range(int(input())):
    cmd = [i for i in input().strip().split()]
    if cmd[0]=="append":
        d.append(cmd[1])
    elif cmd[0]=="appendleft":
        d.appendleft(cmd[1])
    elif cmd[0]=="pop":
        d.pop()
    elif cmd[0]=="popleft":
        d.popleft()

print(" ".join(x for x in d))
