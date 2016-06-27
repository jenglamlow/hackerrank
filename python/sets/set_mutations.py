n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    cmd, num = input().strip().split(" ")
    B = set(map(int, input().split()))

    if cmd == "intersection_update":
        s &= B
    elif cmd == "update":
        s |= B
    elif cmd == "symmetric_difference_update":
        s ^= B
    elif cmd == "difference_update":
        s -= B
print(sum(s))
