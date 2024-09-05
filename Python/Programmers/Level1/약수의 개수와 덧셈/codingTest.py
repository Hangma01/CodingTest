def solution(left, right):
    
    s = 0
    for i in range(left,right+1):
        if len([j for j in range(1, i+1) if i % j == 0]) % 2 == 0:
            s += i
        else:
            s -= i

    return s 

left=13
right=17
print(solution(left,right))