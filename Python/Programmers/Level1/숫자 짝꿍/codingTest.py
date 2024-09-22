from collections import Counter

def solution(X, Y):
    X_Counter = Counter(X)
    Y_Counter = Counter(Y)

    result = list((X_Counter&Y_Counter).elements())

    if not result:
        return '-1'
    elif set(result) == {'0'}:
        return '0'
    
    result.sort(reverse=True)

    return ''.join(result)


X="5525"
Y="1255"
print(solution(X,Y))