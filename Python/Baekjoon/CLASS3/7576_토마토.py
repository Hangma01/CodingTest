import sys
from collections import deque

input = sys.stdin.readline

M, N = list(map(int, input().split()))

graph = [list(map(int, input().split())) for _ in range(N)]
direction = [(-1,0), (1,0), (0,-1), (0,1)]

def BFS():
    
    while Q:
        x, y = Q.popleft()
        
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                Q.append((nx,ny))

Q = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            Q.append((i,j))
            
BFS()

day = 0
cannot_complete = False

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            cannot_complete = True
        day = max(day, graph[i][j])

if cannot_complete:
    print(-1)
else:
    print(day - 1)