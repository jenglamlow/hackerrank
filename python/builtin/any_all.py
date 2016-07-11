A, N = input(), input().split()
print(all(int(i)>0 for i in N) and any(i[::-1]==i for i in N))