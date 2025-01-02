import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

graph = []
Q = deque([])
visited = [[False] * M for _ in range(N)]
result = [[-1] * M for _ in range(N)]
direction = [(-1,0), (1,0), (0,-1), (0,1)]

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(M):
        if row[j] == 2:
            result[i][j] = 0
            Q.append((i,j))
        elif row[j] == 0:
            result[i][j] = 0
    
    graph.append(row)

while Q:
    x, y = Q.popleft()

    for dx, dy in direction:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
            visited[nx][ny] = True
            result[nx][ny] = result[x][y] + 1
            Q.append((nx,ny))

for i in range(N):
    print(*result[i], sep=" ")
