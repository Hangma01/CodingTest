N = int(input())

for _ in range(N):
    count, idx = map(int, input().split())
    data = list(map(int, input().split()))

    result = 1
    while data:
        if data[0] < max(data):
            data.append(data.pop(0))
        else:
            if idx == 0:
                break
            data.pop(0)
            result += 1
        idx = idx - 1 if idx > 0 else len(data) -1
    
    print(result)