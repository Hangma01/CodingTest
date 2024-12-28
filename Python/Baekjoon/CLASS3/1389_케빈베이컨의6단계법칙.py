import sys
from collections import deque

def BFS(v):
    visited = [False] * (N+1)
    distance = [0] * (N + 1)
    visited[v] = True
    cnt = 0
    Q = deque([v])

    while Q:
        q = Q.popleft()

        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                Q.append(i)
                distance[i] = distance[q] + 1
                cnt += 1

    return sum(distance[1:])



N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A) 


result = []
for i in range(1,N+1):
    result.append(BFS(i))

print(result.index(min(result)) + 1)