def solution(babbling):
    answer=["aya","ye","woo","ma"]
    answerNo=["ayaaya","yeye","woowoo","mama"]
    count=0
    
    for babble in babbling:
        for st in answerNo:
            if babble.find(st) > -1:
                break
        else:
            for i in range(len(answer)):
                babble = babble.replace(answer[i],'') 
                 
        if not babble:
            count += 1 
    return count

babbling=["yeayaye"]

print(solution(babbling))