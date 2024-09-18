def solution(babbling):
    answer=["aya","ye","woo","ma"]
    count=0
    
    for babble in babbling:
        for st in answer:
            if st*2 not in babble:
                babble = babble.replace(st,' ')
        
        if babble.isspace():
            count += 1
                
    return count

babbling=["mwooa", "aya"]

print(solution(babbling))