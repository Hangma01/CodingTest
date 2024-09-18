def solution(lottos, win_nums):
    rank = {0 : 6, 1 : 6, 2 : 5, 3 : 4, 4 : 3, 5 : 2,  6 : 1}
    
    bingo=0
    for lotto in lottos:
        if lotto in win_nums:
            win_nums.remove(lotto)
            bingo += 1

    maxBingo = bingo + lottos.count(0) 
    
    return [rank[maxBingo], rank[bingo]]
    

lottos=[45, 4, 35, 20, 3, 9]
win_nums=[20, 9, 3, 45, 4, 35]
print(solution(lottos,win_nums))