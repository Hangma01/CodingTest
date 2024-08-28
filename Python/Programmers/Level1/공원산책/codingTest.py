def solution(park, routes):

    w = len(park)
    h = len(park[0])
    x, y = 0, 0
    op = {"N" : (-1,0), "S" : (1,0), "E" : (0,1), "W" : (0,-1)}
    
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                x, y = i, j
                break
        if park[i][j] == "S":
            break
    
    
    
    for route in routes:
        d, n = route.split()
        dx, dy = x, y
        
        for i in range(int(n)):
            nx = x + op[d][0]
            ny = y + op[d][1]

            if 0 <= nx < w and 0 <= ny < h and park[nx][ny] != "X":
                x, y = nx, ny
            else:
                x, y = dx, dy
                break
        
    return [x,y]

park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]

print(solution(park,routes))