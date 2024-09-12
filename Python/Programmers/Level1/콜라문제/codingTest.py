def solution(a, b, n):

    count = 0
    while n >= a:
        exchange = n//a*b 
        count += exchange
        n = n%a + exchange
    
    return count

a=3
b=1
n=20
print(solution(a,b,n))