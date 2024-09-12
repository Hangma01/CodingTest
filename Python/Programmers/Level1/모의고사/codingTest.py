def solution(answers):
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    
    aCnt=0
    bCnt=0
    cCnt=0

    aa=[]
    bb=[]
    cc=[]

    for i in range(len(answers)):
        aa.append(a[i%len(a)])
        bb.append(b[i%len(b)])
        cc.append(c[i%len(c)])
   

    for i in range(len(answers)):
       
        if aa[i] == answers[i]:
            aCnt +=1
        if bb[i] == answers[i]:
            bCnt +=1
        if cc[i] == answers[i]:
            cCnt +=1
    
    
    item = {1 : aCnt, 2 : bCnt, 3 : cCnt}
    maxVal = max(item.values())

    return [key for key, value in item.items() if value == maxVal]

answers=[1, 3, 2, 4, 2, 4, 5, 6]
print(solution(answers))