s = input()
pos = input().split()
print(s[:int(pos[0])] + pos[1] + s[int(pos[0])+1:])