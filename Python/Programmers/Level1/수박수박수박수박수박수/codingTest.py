def solution(n):
    text="수박"
    
    return ''.join(text[i%2] for i in range(n))

n=3
print(solution(n))