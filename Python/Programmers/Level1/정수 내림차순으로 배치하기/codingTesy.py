def solution(n):
    num_list = list(str(n))
    num_list.sort(reverse=True)
    result = ''.join(num_list)
   
    return int(result)
    

n = 118372
print(solution(n))