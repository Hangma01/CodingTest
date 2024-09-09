def solution(array, commands):
    answer = []
    for com in commands:
        arr = array[com[0]-1:com[1]]
        arr.sort()
        answer.append(arr[com[2]-1])

    return answer

array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array,commands))