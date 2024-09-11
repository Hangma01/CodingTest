def solution(n, arr1, arr2):
    result = []

    for i, j in zip(arr1, arr2):
        map1 = bin(i)[2:].zfill(n)
        map2 = bin(j)[2:].zfill(n)
   
        s = ['#' if (int(map1[k:k+1]) | int(map2[k:k+1])) else ' ' for k in range(n)]
        result.append(''.join(s))
    
    return result
        


n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]

print(solution(n,arr1,arr2))