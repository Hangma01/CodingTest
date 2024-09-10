from itertools import combinations

def solution(numbers):

    answer=[]
    for i in combinations(numbers,2):
        
        if sum(i) not in answer:
            answer.append(sum(i))

    return sorted(answer)

numbers=[2,1,3,4,1]
print(solution(numbers))