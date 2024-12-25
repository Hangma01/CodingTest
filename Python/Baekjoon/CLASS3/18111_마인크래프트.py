import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

leastTime = 10**8

minHeight = min(map(min, graph))
maxHeight = max(map(max, graph))

totalHeight = minHeight

for floor in range(minHeight, maxHeight+1):
    plusFloor = 0
    minusFloor = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > floor:
                minusFloor += graph[i][j] - floor
            else:
                plusFloor += floor - graph[i][j]
    
    if minusFloor + B >= plusFloor:
        
        time = minusFloor * 2 + plusFloor
        
        if leastTime >= time:
            leastTime = time
            totalHeight = floor
            
print(leastTime, totalHeight)

