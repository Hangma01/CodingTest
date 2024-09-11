def solution(food):

    s = [str(idx)*(i//2) for idx, i in enumerate(food) if i != 1]
    s = ''.join(s)
    
    return s + '0' + s[::-1]

food=[1,3,4,6]
print(solution(food))