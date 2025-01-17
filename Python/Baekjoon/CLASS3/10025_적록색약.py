import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [list(input().strip()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
color_blindness_visited = [[0] * N for _ in range(N)]

direction = [(-1,0), (1,0), (0,-1), (0,1)]

def BFS(i, j, word):

    visited[i][j] = 1
    Q = deque()
    Q.append((i,j))
    
    while Q:
        
        x, y = Q.popleft()
        
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
    
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if graph[nx][ny] == word:
                    visited[nx][ny] = 1
                    Q.append((nx,ny))
                    
def color_blindness_bfs(i, j, word):
    color_blindness_visited[i][j] = 1
    Q = deque()
    Q.append((i,j))
    
    color_blindness = False
    
    if word == 'R' or word == 'G':
        color_blindness = True
    
    while Q:
        
        x, y = Q.popleft()
        
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
    
            if 0 <= nx < N and 0 <= ny < N and color_blindness_visited[nx][ny] == 0:
                if color_blindness:
                    if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                        color_blindness_visited[nx][ny] = 1
                        Q.append((nx,ny))
                else:
                    if graph[nx][ny] == 'B':
                        color_blindness_visited[nx][ny] = 1
                        Q.append((nx,ny))


count = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            word = graph[i][j]
            count += 1
            BFS(i,j,word)

color_blindness_count = 0
for i in range(N):
    for j in range(N):
        if color_blindness_visited[i][j] == 0:
            word = graph[i][j]
            color_blindness_count += 1
            color_blindness_bfs(i,j,word)

print(count, color_blindness_count)

