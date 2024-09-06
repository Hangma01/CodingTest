def solution(d, budget):
    return len([i for i in range(1,len(d)+1) if sum(sorted(d)[:i]) <= budget])


d=[2, 2, 3, 3]
budget=10
print(solution(d,budget))


    