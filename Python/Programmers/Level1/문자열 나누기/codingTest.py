def solution(s):
    preCount=0
    nextCount=0
    result=0
    preWord=''
    for idx, st in enumerate(s):
        
        if idx == 0:
            preWord=s[idx]

        if preWord != st:
            nextCount += 1
        else:
            preCount += 1
        
        if preCount == nextCount:
            result += 1
            preWord=s[idx+1:idx+2]
            preCount=0
            nextCount=0
        elif idx+1 == len(s):
            result += 1


    return result


s="abaabab"
print(solution(s))