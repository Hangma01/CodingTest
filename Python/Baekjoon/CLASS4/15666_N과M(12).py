import sys

input = sys.stdin.readline

N, M = map(int, input().split())

seq = sorted(map(int, input().split()))
data = []

def DFS(num):
    
    if len(data) == M:
        print(*data)
        return
    
    temp = 0
    for i in range(N):
        if num <= seq[i] and temp != seq[i]:
            data.append(seq[i])
            temp = seq[i]
            DFS(temp)
            data.pop()

            
DFS(0)