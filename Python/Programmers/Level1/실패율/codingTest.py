def solution(N, stages):
    
    failureRate={}
    for i in range(1,N+1):
        if i in stages:
            count = len(list(filter(lambda x: x >= i, stages)))
            failureRate[i] = stages.count(i) / count
        else:
            failureRate[i] = 0
        
    failureRate = dict(sorted(failureRate.items(), key= lambda x:x[1], reverse=True))

    return list(failureRate.keys())

N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N,stages))