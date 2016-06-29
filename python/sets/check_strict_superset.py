A = set(input().split(" "))
check = True
for i in range(int(input())):
    B = set(input().split()) 
    check = check and B.issubset(A)
    
print(check)

# From Discussion (Pythonic Way)
# a = set(input().split())
# print(all(a > set(input().split()) for _ in range(int(input()))))