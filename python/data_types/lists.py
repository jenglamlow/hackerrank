N = int(input())

L = []

for i in range(N):
    command = input()

    command = command.split()
    cmd = command[0]
    if cmd == "insert":
        L.insert(int(command[1]), int(command[2]))
    elif cmd == "remove":
        L.remove(int(command[1]))
    elif cmd == "append":
        L.append(int(command[1]))
    elif cmd == "sort":
        L.sort()
    elif cmd == "reverse":
        L.reverse()
    elif cmd == "pop":
        L.pop()
    elif cmd == "print":
        print(L)