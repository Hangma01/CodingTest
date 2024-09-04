def solution(arr, divisor):
    answer = []

    [answer.append(i) for i in arr if i % divisor == 0]

    if not len(answer):
        answer.append(-1)
        return answer

    answer.sort()

    return answer

arr=[2, 36, 1, 3]
divisor=1
print(solution(arr,divisor))