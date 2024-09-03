def solution(arr):
    
    result = sum(i for i in arr) / len(arr)

    return result

arr = [1,2,3,4]
print(solution(arr))