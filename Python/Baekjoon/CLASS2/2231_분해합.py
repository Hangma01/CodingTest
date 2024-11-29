N = int(input())

result = 0
for i in range(1, N+1):
    constructor = i + sum(map(int, str(i)))

    if constructor == N:
        result = i
        break

print(result)