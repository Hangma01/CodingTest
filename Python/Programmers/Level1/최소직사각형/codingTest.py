def solution(sizes):
    reSizes = [[max(w,h),min(w,h)] for w, h in sizes]
    
    width = max([size[0] for size in reSizes])
    height = max([size[1] for size in reSizes])
    
    return width * height


sizes=[[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))