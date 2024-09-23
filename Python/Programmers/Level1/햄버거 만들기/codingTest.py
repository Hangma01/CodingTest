def solution(ingredient):
    sample=[1,2,3,1]
    i = 0
    count = 0
    while i < (len(ingredient)-3):
        
        if ingredient[i:i+4] == sample:
            del ingredient[i:i+4]  # 시간 복잡도가 있네  
            i = 0
            count += 1
        else:
            i += 1
    
    return count
    


ingredient=[1, 3, 2, 1, 2, 1, 3, 1, 2]
print(solution(ingredient))