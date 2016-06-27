vowel = "AEIOU"

s = input()

kevin = 0
stuart = 0

for i in range(len(s)):
    if s[i] in vowel:
        kevin += len(s) - i
    else:
        stuart += len(s) - i

if kevin > stuart:
    print("Kevin", kevin)
elif stuart > kevin:
    print("Stuart", stuart)
else:
    print("Draw")