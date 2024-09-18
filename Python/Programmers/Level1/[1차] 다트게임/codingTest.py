def solution(dartResult):
    score = []
    point = ""
    for st in dartResult:
        size = len(score)
        if st.isnumeric():
            point += st
            continue
        elif(st == "*"):
            score[size-1] *= 2
            if size != 1 :
                score[size-2] *= 2
        elif(st == "#"):
            score[size-1] *= -1
        elif(st=="S"):
            score.append(int(point)**1)
        elif(st=="D"):
            score.append(int(point)**2)
        elif(st=="T"):
            score.append(int(point)**3)
        print(score)
        point = ""

    return sum(score)

dartResult="1D2S#10S"
print(solution(dartResult))