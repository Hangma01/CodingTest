import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for i in range(N+1)]
dfsVisited=[0]*(N+1)
bfsVisited=[0]*(N+1)

#DFS(깊이 탐색)
def DFS(v):
    dfsVisited[v] = 1
    print(v, end=' ')

    for i in graph[v]:
        if dfsVisited[i] == 0:
            dfsVisited[i] = 1

            DFS(i)

#BFS(너비 탐색)
def BFS(v):
    Q = deque([v])
    bfsVisited[v] = 1
    while Q:
        q = Q.popleft()
        print(q, end=' ')
        for i in graph[q]:
            if bfsVisited[i] == 0:
                bfsVisited[i] = 1
                Q.append(i)

              

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(N + 1):
    graph[i].sort()

DFS(V)

print()
BFS(V)

