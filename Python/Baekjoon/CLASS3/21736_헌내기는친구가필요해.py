import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# DFS
def dfs(x,y):
    global cnt
    visited[x][y] = True
    
    if graph[x][y] == 'P':
        cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if graph[nx][ny] != 'X':
                dfs(nx,ny)

# BFS
def bfs(x,y):
    global cnt
    visited[x][y] = True

    Q = deque([(x,y)])

    while Q:
        
        x, y = Q.popleft()

        if graph[x][y] == 'P':
            cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if graph[nx][ny] != 'X':
                    visited[nx][ny] = True
                    Q.append((nx,ny))



dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
N, M = map(int, input().split())
graph = list(input().strip() for _ in range(N))
visited = [[False] * M for _ in range(N)]
      

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            #dfs(i,j)
            bfs(i,j)

if cnt == 0:
    print("TT")
else:
    print(cnt)