N = int(input())
K = [int(i) for i in input().strip().split(" ")]
S = set(K)

# (1,2,3,4,5) * N - [list] = missing value * (N-1)
print((sum(S) * N - sum(K))//(N-1))