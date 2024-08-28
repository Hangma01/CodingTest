def solution(players, callings):
    
    answer = []
    rank = {player: idx for idx, player in enumerate(players)}

    for call in callings:
        index = rank[call]
        rank[call] -= 1
        rank[players[index-1]] += 1
        players[index], players[index-1] = players[index-1], players[index]
   
    answer = players
    
    return answer

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))