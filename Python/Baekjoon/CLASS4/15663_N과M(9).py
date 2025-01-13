import sys

input = sys.stdin.readline

N, M = map(int, input().split())

seq = sorted(map(int, input().split()))
data = []
visited = [False] * N

def DFS():
    
    if len(data) == M:
        print(*data)
        return
    
    temp = 0
    for i in range(N):
        if not visited[i] and temp != seq[i]:
            data.append(seq[i])
            visited[i] = True
            temp = seq[i]
            DFS()
            data.pop()
            visited[i] = False
            
DFS()