import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = list(input().strip() for _ in range(N))
visited = [[0] * M for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    Q = deque([(0,0)])
    visited[0][0] = 1

    while Q:
        x, y = Q.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y]
        
       
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == '1':
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append((nx,ny))


print(bfs())
            