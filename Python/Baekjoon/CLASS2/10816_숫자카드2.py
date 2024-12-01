N = int(input())
nMums = map(int,input().split())

dict={}
for num in nMums:
    dict[num] = dict.get(num, 0) + 1
    
M = int(input())
mNums = map(int, input().split())

result = []
for num in mNums:
    result.append(dict.get(num,0))

print(*result)
