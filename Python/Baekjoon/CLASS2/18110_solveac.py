import sys

N = int(sys.stdin.readline())

if N == 0:
    print(0)
else:
    avg = int((N*0.15)+0.5)

    levels = []
    for _ in range(N):
        levels.append(int(sys.stdin.readline()))

    levels.sort()

    print(int((sum(levels[avg:N-avg]) / (len(levels[avg:N-avg]))) + 0.5))
