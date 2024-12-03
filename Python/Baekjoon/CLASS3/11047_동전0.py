N, M = map(int, input().split())

coins = []
result = 0
for _ in range(N):
    coins.append(int(input()))

for coin in sorted(coins,reverse=True):
    result += M//coin
    M %= coin

print(result)
