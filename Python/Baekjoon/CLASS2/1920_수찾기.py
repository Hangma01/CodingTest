import sys

input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for find in B:
    if find in A:
        print(1)
    else:
        print(0)