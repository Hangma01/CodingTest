import sys
from collections import deque


input = sys.stdin.readline

N = int(input())

parent = [0] * (N+1)
dic = {i : [] for i in range(N+1)}

def BFS(v):
    Q = deque([v])
    
    while Q:
        q = Q.popleft()
        
        for i in dic[q]:
            if parent[i] == 0:
                parent[i] = q
                Q.append(i)


for _ in range(N-1):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)


BFS(1)

for i in range(2, N+1):
    print(parent[i])