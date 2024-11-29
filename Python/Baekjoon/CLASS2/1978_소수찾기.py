N = int(input())
numArr = list(map(int, input().split()))

result = 0
for num in numArr:

    if num == 1:
        continue

    for i in range(2, num):
        if num % i == 0:
            break
    else:
        result += 1

print(result)