import sys

N = int(sys.stdin.readline())

count = 0
stack = []
result = []
isFalse = False
for i in range(1, N+1):
    num = int(sys.stdin.readline())

    while count < num:
        count += 1
        stack.append(count)
        result.append("+")

    if stack[-1] == num:
        stack.pop()
        result.append("-")  
    else:
        print("NO")
        isFalse = True
        break


if not isFalse: 
    for i in result:
        print(i)
