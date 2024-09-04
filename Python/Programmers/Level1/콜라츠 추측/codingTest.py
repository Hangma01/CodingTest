def collatz(num):

    if num == 1:
        return 0
    elif num % 2 == 0:
        num = num/2
    else:
        num = (num*3) +1

    return 1 + collatz(num)

def solution(num):
   
    result = collatz(num)
    
    if result > 500:
        return -1
    
    return result

num = 626331
print(solution(num))