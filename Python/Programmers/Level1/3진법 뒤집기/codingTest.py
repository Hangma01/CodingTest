def solution(n):
    s=[]

    while n > 0:
        s.append(n%3)
        n = n // 3

    result = sum(s[-i]*3**(i-1) for i in range(1,len(s)+1))
    
    return result

n=45
print(solution(n))
print(2.2 == True)