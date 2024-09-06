def solution(arr1, arr2):
    
    return [[x+y  for x,y in zip(arr1[i], arr2[i])] for i in range(len(arr1))]

arr1=[[1,2],[2,3]]
arr2=[[3,4],[5,6]]
print(solution(arr1,arr2))

