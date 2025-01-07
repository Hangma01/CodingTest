import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    
    rev = False
    flag = False
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')
    
    if n == 0:
        Q = []
    else:
        Q = deque(arr)

    for str in p:
        if str == 'R':
            rev = not rev
        elif str == 'D':
            if len(Q) < 1:
                flag = not flag
                print('error')
                break
            else:
                if rev:
                    Q.pop()
                else:
                    Q.popleft()
    
    if not flag:
        if rev:
            Q.reverse()
            print('[' + ','.join(Q) + ']')
        else:
            print('[' + ','.join(Q) + ']')