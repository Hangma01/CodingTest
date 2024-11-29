count = int(input())
scores = list(map(int,input().split()))

totalScore = 0
for score in scores:
    totalScore += score/max(scores)*100

print(round(totalScore/count,6))