import sys
input = sys.stdin.readline
N, M = map(int, input().split())
data = list(map(int, input().split()))
sum = [0]
tmp = 0

for i in data:
    tmp += i
    sum.append(tmp)

for _ in range(M):
    first, last = map(int, input().split())
    print(sum[last] - sum[first-1])