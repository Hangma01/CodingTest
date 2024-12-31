import sys
from collections import deque
input = sys.stdin.readline

def BFS(x,y):
    cnt = 1
    visited[x][y] = True

    Q = deque([(x,y)])

    while Q:
        a, b = Q.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] == '1':
                    
                    visited[nx][ny] = True
                    cnt += 1
                    Q.append((nx,ny))

    return cnt



N = int(input())

graph = list(input().strip() for _ in range(N))
visited = [[False] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == '1':
            result.append(BFS(i,j))
print(len(result))
result.sort()
print(*result, sep='\n')