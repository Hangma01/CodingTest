import sys

N = int(input().strip())

data = []
for _ in range(N):
    a, b = map(int, input().split())
    data.append((a,b))

data = sorted(data, key = lambda x : (x[1], x[0]))

time = 0
count = 0
for start, end in data:
    if time <= start:
        time = end
        count += 1
    
print(count)