from itertools import product
A = [int(i) for i in input().split(" ")]
B = [int(i) for i in input().split(" ")]
print(*list(product(A,B)), sep=" ")