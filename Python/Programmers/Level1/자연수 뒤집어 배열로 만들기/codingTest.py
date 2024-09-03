def solution(n):
    result = list(int(i) for i in str(n)[::-1])
    
    return result
    
    

n = 12345
print(solution(n))