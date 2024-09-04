def solution(x):
    listX = list(map(int, str(x)))
    if x % sum(i for i in listX) == 0:
        return True
    
    return False

x = 13
print(solution(x))