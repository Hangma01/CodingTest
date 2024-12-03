import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dataName = {}
dataNum = {}
for i in range(N):
    name = input().rstrip()
    dataNum[i] = name
    dataName[name] = i+1
for _ in range(M):
    enter = input().rstrip()
    if enter.isdigit():
        print(dataNum[int(enter) -1])
    else:
        print(dataName[enter])
