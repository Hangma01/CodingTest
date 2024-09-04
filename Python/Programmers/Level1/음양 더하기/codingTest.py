def solution(absolutes, signs):
    result = 0

    for index, i in enumerate(absolutes):
        if not signs[index]:
            absolutes[index] = absolutes[index]*-1
        result += absolutes[index]

    return result


absolutes=[1,2,3]
signs=[False,False,True]
print(solution(absolutes,signs))