import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):
            if data[ny][nx]:
                data[ny][nx] = 0
                dfs(nx,ny)

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    data = [[0]*M for i in range(N)]
    count = 0

    for i in range(K):
        x,y = map(int, sys.stdin.readline().split())
        data[y][x] = 1

    for x in range(M):
        for y in range(N):
            if data[y][x] == 1:
                dfs(x,y)
                count += 1

    print(count)
