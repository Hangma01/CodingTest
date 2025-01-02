import sys
sys.setrecursionlimit(10**6)


def DFS(v):

    for i in range(N):

        if graph[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            DFS(i)

N = int(sys.stdin.readline())

graph = [list(map(int,sys.stdin.readline().split())) for i in range(N)]


for i in range(N):
    visited = [0] * N
    DFS(i)
    print(*visited, sep=" ")