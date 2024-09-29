def solution(today, terms, privacies):
    today = list(map(int, today.split('.')))
    terms = {i[0]: int(i[2:])for i in terms}
    
    today = today[0] * 28 * 12 + today[1] * 28 + today[2] 

    answer = []
    for i, pri in enumerate(privacies):
        day, kind = pri.split()
        month = terms[kind]
        day = list(map(int, day.split('.')))
        day = day[0] * 28 * 12 + day[1] * 28 + day[2]-1 + month * 28 
        
        if day < today:
            answer.append(i+1)
                    
    return answer

today="2022.05.19"
terms=["A 6", "B 12", "C 3"]
privacies=["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))