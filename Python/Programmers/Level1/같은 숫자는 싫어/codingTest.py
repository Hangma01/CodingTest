def solution(arr):
    result = [arr[0]]
    result += [arr[i] for i in range(1,len(arr)) if arr[i-1] != arr[i]]
    
    return result

arr=[1,1,3,3,0,1,1]
print(solution(arr))
