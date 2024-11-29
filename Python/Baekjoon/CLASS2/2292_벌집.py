N = int(input())

count = 0
num = 1
result = 1
while True:
    
    num += 6 * count
    if N <= num:
        break
        
    count += 1   

print(result + count)