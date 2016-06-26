N = int(input())
L = []
for student in range(N):
    L.append([input(), float(input())])

second_highest = sorted(set([marks for name, marks in L]), reverse=True)[-2]

for name, marks in sorted(L):
    if marks == second_highest:
        print(name)

# Clever print
# print('\n'.join([a for a,b in sorted(L) if b == second_highest]))