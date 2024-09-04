def solution(n):
    
    sqrt = n**(1/2)

    if sqrt.is_integer():
        return pow(int(sqrt+1),2)
    
    return -1

n = 121
print(solution(n))

