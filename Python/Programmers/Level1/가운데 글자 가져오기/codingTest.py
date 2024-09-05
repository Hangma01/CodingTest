import math

def solution(s):
    s = list(s)
    sLen = len(s)

    if len(s) % 2 == 0:
        return s[sLen//2-1] + s[sLen//2]
    else:
        return s[sLen//2]
    
s="abcde"
print(solution(s))