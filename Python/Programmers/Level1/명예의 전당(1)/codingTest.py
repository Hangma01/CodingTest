def solution(k, score):
    
    rank = []
    result = []
    
    for i in score:
        rank.append(i)
        rank = sorted(rank, reverse=True)[:k]
        result.append(rank[len(rank)-1])

    return result
    

k=4
score=[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
print(solution(k,score))