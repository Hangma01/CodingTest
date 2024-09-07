def solution(number):
    
    result = 0
    
    for i in range(len(number)-2):
        for j in range(i+1,len(number)):
            for k in range(j+1,len(number)):
                if number[i] + number[j] + number[k] == 0:
                    result += 1 

    return result

number=[-3, -2, -1, 0, 1, 2, 3]
print(solution(number))