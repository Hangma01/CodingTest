import sys


def func(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return func(x-1) + func(x-2) + func(x-3)

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(input())
    print(func(num))