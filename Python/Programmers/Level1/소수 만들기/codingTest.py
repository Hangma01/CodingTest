from itertools import combinations as cb

def solution(nums):

    result = 0

    for nCr in cb(nums,3):
        nCrSum = sum(nCr)
        for i in range(2,int(nCrSum**0.5)+1):
            if nCrSum % i == 0 :
                break
        else:
            result +=1
        
    return result

nums=[1,2,7,6,4]

print(solution(nums))