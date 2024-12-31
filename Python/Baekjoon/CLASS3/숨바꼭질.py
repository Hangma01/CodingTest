from collections import deque

N, M = map(int, input().split())
maxNum = 100001
visited = [0] * (maxNum)


def bfs():
    Q = deque([N])

    while Q:
        q = Q.popleft()
        
        if q == M:
            return visited[q]
        
        for i in (q-1, q+1, q*2):
            if 0 <= i < maxNum and not visited[i]:
                visited[i] = visited[q] + 1
                Q.append(i)

print(bfs())