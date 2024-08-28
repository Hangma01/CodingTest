def solution(n, m, section):
    answer = 0

    val = section[0]
    answer += 1

    for i in section:
        if i >= val + m:
            answer += 1
            val = i

    return answer



n = 4
m = 1
section = [1, 2, 3, 4]

print(solution(n,m,section))