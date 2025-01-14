import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())

def BFS():
    Q = deque([(A,1)])
    
    while Q:
        q, cnt = Q.popleft()
        
        if q == B:
            return cnt
        
        nums = [q*2, q*10+1]
        for i in nums:
            if i <= B:
                Q.append((i,cnt+1))
    
    return -1
                
    
print(BFS())