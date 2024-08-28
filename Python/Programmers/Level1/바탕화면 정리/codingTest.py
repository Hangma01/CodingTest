def solution(wallpaper):
    answer = []

    lux = 0
    luy = 0
    rdx = 0
    rdy = 0
    check = False
    
    for idx, wallpa in enumerate(wallpaper):
        x = idx
        ly = wallpa.find('#')
        ry = wallpa.rfind('#')

        if ly == -1:
            continue
        elif check == False:
            lux = x
            luy = ly
            rdx = x + 1
            rdy = ry + 1
            check = True
        
            
        if x < lux:
            lux = x

        if ly < luy:
            luy = ly

        if x >= rdx:
            rdx = x + 1

        if ry >= rdy:
            rdy = ry + 1
    
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx)
    answer.append(rdy)

    return answer

wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]

print(solution(wallpaper))