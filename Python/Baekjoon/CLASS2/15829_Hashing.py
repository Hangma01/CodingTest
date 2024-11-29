L = int(input())
M = 1234567891
r = 31

userInput = input()

result = 0
for i in range(L):
    num = ord(userInput[i]) - 96
    result += num * (r**i)

print(result % M)