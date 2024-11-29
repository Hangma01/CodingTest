T = int(input())

for t in range(T):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]

    for x in range(k):
        for i in range(1,n):
            people[i] += people[i-1]
    print(people[-1])