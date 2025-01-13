import sys
from collections import deque

input = sys.stdin.readline

def BFS():
            
    Q = deque([1])
    
    while Q:
        q = Q.popleft()
        
        if q == 100:
            print(board[q])
            break
            
        for i in range(1, 7):
            next = q + i
            if 0 < next <= 100 and board[next] == 0:
                if next in ladders.keys():
                    next = ladders[next]
                elif next in sankes.keys():
                    next = sankes[next]
                    
                if board[next] == 0:
                    board[next] = board[q] + 1
                    Q.append(next)



N, M = map(int, input().split())
board = [0] * 101

ladders = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y

sankes = {}
for _ in range(M):
    x, y = map(int, input().split())
    sankes[x] = y

BFS()   
