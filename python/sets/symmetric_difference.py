n, A, m, B = (set([int(i) for i in input().strip().split(" ")]) for _ in range(4))
print(len(A.symmetric_difference(B)))