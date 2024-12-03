import sys
input = sys.stdin.readline
N = int(input())

times = sorted(list(map(int, input().split())))

result = 0
for i in range(1, N+1):
    result += sum(times[:i])

print(result)