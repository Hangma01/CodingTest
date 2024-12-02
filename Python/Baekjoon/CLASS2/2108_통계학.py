import sys

def custom_round(value):
    return int(value + 0.5) if value > 0 else int(value - 0.5)

N = int(sys.stdin.readline())

data = []
count = {}
for _ in range(N):
    x = int(sys.stdin.readline())
    data.append(x)

    if x in count:
        count[x] += 1
    else:
        count[x] = 1

data.sort()

# 산술평균
print(custom_round(sum(data) / len(data)))

# 중앙값
print(data[len(data)//2])

# 최빈값
freq = max(count.values())
numbers = []
for key, value in count.items():
    if value == freq:
        numbers.append(key)


if len(numbers) > 1 :
    print(sorted(numbers)[1])
else:
    print(numbers[0])

# 범위
print(data[-1]-data[0])
