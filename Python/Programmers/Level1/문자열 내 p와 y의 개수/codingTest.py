def solution(s):
    
    p, y = (lambda s: (sum(1 for i in s if i == 'p'), sum(1 for i in s if i == 'y')))(s.lower())

    if p == y:
        return True
    
    return False


s = 'Hello Python'

print(solution(s))