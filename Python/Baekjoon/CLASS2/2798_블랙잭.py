from itertools import combinations

N, Max = map(int, input().split())
nums = list(map(int,input().split()))
result = 0
for cards in combinations(nums,3):
    sumCards = sum(cards)
    if(sumCards) <= Max:
        result = max(result,sumCards)

print(result)
