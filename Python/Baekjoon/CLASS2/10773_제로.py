N = int(input())

stack = []
for i in range(N):
    m = int(input())

    if m == 0:
        stack.pop()
    else:
        stack.append(m)

print(sum(stack))