import sys
input = sys.stdin.readline

N = int(input())

positions = [list(map(int, input().split())) for _ in range(N)]

positions.sort()

for x, y in positions:
    print(x, y)