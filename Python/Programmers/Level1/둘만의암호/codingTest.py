def solution(s, skip, index):

    answer = ''

    skipList = list(skip)
     
    for ch in s:
        
        count = 0
        currentChr = ch

        while count < index:
            currentChr = chr(ord(currentChr) + 1)

            if currentChr > 'z':
                currentChr = 'a'

            if currentChr not in skipList:
                count += 1
            
        answer += currentChr

    return answer

s = "aukks"
skip = "wbqd"
index = 5


print(solution(s,skip,index))
