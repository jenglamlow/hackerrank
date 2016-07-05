from collections import Counter

input()
income = 0
shoe = Counter([int(i) for i in input().strip().split(" ")])
for _ in range(int(input())):
    size, price = map(int, input().strip().split(" "))
    if shoe[size]:
        income += price
        shoe[size] -= 1

print(income)