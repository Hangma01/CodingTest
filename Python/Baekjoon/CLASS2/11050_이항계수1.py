N, K = map(int, input().split())

def factorial(num):
    if num > 1:
        return num * factorial(num -1)
    else:
        return 1
        
print(factorial(N)//(factorial(K)*factorial(N-K)))