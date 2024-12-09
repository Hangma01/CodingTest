import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    num = int(input())
    dp = [0] *(num+1) 

    for i in range(1,num+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 1
        elif i == 3:
            dp[i] = 1
        else:
            dp[i] = dp[i-2] + dp[i-3]
    print(dp[num])
