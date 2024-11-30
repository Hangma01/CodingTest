import sys
input = sys.stdin.readline

N = int(input())

person = [list(input().split()) for _ in range(N)]

person.sort(key = lambda x : int(x[0]))

for age, name in person:
    print(age, name)