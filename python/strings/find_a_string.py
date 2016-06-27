s, ss = (input() for _ in range(2))
index = 0
count = 0
while index < len(s):
    index = s.find(ss, index)
    if index == -1:
        break
    count += 1
    index += 1
print(count)

# From discussion
count = 0
for i in range(len(s)):
    if s[i:i+len(ss)] == ss:
        count += 1
