import sys
N = int(sys.stdin.readline())

data = []
for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "add":
        if int(command[1]) not in data:
            data.append(int(command[1]))
    elif command[0] == "remove":
        if int(command[1]) in data:
            data.remove(int(command[1]))
    elif command[0] == "check":
        if int(command[1]) in data:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if int(command[1]) in data:
            data.remove(int(command[1]))
        else:
            data.append(int(command[1]))
    elif command[0] == "all":
        data.clear()
        for i in range(1,21):
            data.append(i)
    elif command[0] == "empty":
        data.clear()