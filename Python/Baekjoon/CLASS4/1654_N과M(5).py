import sys

N, M = map(int, sys.stdin.readline().split())

seq = sorted(map(int, sys.stdin.readline().split()))
data = []
def DFS(num):
    
    if len(data) == M:
        print(*data)
        return
    
    for i in range(N):
        if seq[i] not in data:
            data.append(seq[i])
            DFS(num+1)
            data.pop()

DFS(0)