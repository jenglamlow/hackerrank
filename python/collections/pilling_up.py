from collections import deque

d = deque()
so = []
for _ in range(int(input())):  
    n = int(input())
    cubes = deque(map(int, input().split()))
    top = cubes.popleft() if cubes[0] > cubes[-1] else cubes.pop()
    while cubes:
        left, right = cubes[0], cubes[-1]
        if left >= right and left <= top:
            top = cubes.popleft()
        elif right > left and right <= top:
            top = cubes.pop()
        else:
            print("No")
            break
    if len(cubes) == 0:
        print("Yes")

# Without deque method (From discussion rawmaze)
for t in range(input()):
    input()
    lst = map(int, raw_input().split())
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    if i == l - 1:
        print ("Yes") 
    else:
        print("No")

# From sumer96
t = int(input())
for v in range (t):
    a = 0
    n = int(input())
    d = [int(x) for x in input().split()]
    for i in range(int(n/2)):
        if d[i]<d[i+1] and d[n-i-1]<d[n-i-2]:
            print("No")
            a = 1
            break
        else:
            continue
    if a != 1:
        print("Yes")