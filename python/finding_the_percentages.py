N = int(input())

dict = {}

for i in range(N):
    data = input()
    data = data.split()
    dict[data[0]] = [float(i) for i in data[1:]]
    
test = input()

print("{0:.2f}".format(round(sum(dict[test])/len(dict[test]), 2)))