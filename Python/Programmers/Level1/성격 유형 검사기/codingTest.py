def solution(survey, choices):
    index = {0: [1,2,3], 1 : [5,6,7]}
    type = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    score = {1 : 3, 2 : 2, 3 : 1, 5 : 1, 6 : 2, 7 : 3}
    pairs=[('R','T'),('C','F'),('J','M'),('A','N')]
    result=''

    for idx, choice in enumerate(choices):
        if choice in index[0]:
            type[survey[idx][0]] += score[choice]
        elif choice in index[1]:
            type[survey[idx][1]] += score[choice]
    
    
    for a,b in pairs:
        result += max((a, b), key=lambda x: type[x])

    return result


survey=["AN", "CF", "MJ", "RT", "NA"]
choices=[5, 3, 2, 7, 5]
print(solution(survey,choices))