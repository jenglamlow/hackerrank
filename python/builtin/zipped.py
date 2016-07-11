N, X = map(int, input().split())
G = []
for _ in range(X):
    G.append([float(i) for i in input().split()])

print(*[sum(student)/len(student) for student in zip(*G)], sep='\n')