import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = {}
for _ in range(N):
    enter = input().split()
    data[enter[0]] = enter[1]

for _ in range(M):
    enter = input().strip()
    print(data[enter])