import sys

# 입력 받기
n, k = map(int, sys.stdin.readline().split())
idx = 0
queue = [i for i in range(1,n+1)]
result = []
while len(queue):

    idx += k - 1
    if idx >= len(queue):
        idx %= len(queue)
    result.append(str(queue.pop(idx)))

print("<" + ", ".join(result) + ">")