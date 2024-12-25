import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# DFS(깊이 우선 탐색)
def DFS(v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            DFS(i)
    
# BFS(너비 우선 탐색)
def BFS(v):
    visited[v] = True
    
    Q = deque([v])
    while Q:
        q = Q.popleft()
        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                Q.append(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
count = 0
visited = [False] * (N+1)
for i in range(1,N+1):
    if not visited[i]:
        DFS(i)
        count += 1
print(count)

count = 0
visited = [False] * (N+1)
for i in range(1,N+1):
    if not visited[i]:
        BFS(i)
        count += 1
print(count)