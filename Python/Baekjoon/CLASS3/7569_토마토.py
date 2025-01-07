import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

Q = deque()

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    while Q:

        z, y, x = Q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    Q.append((nz,ny,nx))


for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 1:
                Q.append((h,n,m))

bfs()

cannot_complete = False
day = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 0:
                cannot_complete = True
            day = max(day,graph[h][n][m])

if cannot_complete:
    print(-1)
else:
    print(day - 1)