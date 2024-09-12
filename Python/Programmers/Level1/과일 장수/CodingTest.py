def solution(k, m, score):
    score.sort(reverse=True)
    
    return sum([min(score[i*m:i*m+m])*m for i in range(len(score)//m)])


k=4
m=3
score=[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k,m,score))