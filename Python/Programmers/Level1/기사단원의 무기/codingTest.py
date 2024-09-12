def solution(number, limit, power):
    
    result=[]
    for i in range(1,number+1):
        divisor = [i]
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                divisor.append(j)
                divisor.append(i//j)

            if len(set(divisor)) > limit:
                result.append(power)
                break
        else:
            result.append(len(set(divisor)))
            continue
        
    return sum(result)

    
    
   

number=10
limit=3
power=2

print(solution(number,limit,power))