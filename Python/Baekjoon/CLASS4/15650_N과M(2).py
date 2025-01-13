import sys

N, M = map(int, sys.stdin.readline().split())

seq = []
def DFS(start):
    
    if len(seq) == M:
        print(*seq)
        return
    
    for i in range(start, N+1):
        seq.append(i)
        DFS(i+1)
        seq.pop()
    
    
DFS(1)
