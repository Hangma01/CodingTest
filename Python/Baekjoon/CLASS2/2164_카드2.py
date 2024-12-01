from collections import deque

N = int(input())

queue = deque(range(1, N+1))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])


# 공식으로 푸는법
# input = int(input())
# square = 2

# while True:
#     if (input == 1 or input == 2):
#         print(input)
#         break
#     square *= 2
#     if (square >= input):
#         print((input - (square // 2)) * 2)
#         break
