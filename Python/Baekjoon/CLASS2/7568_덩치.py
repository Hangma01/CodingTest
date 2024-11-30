import sys
input = sys.stdin.readline

N = int(input())

sizes = [list(map(int,input().split())) for _ in range(N)]
rank = []
for size in sizes:
    count = 1

    for rest in sizes:
        if size[0] < rest[0] and size[1] < rest[1]:
            count += 1
    
    rank.append(count)

print(*rank)