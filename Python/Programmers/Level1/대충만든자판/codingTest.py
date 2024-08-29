def solution(keymap, targets):
    answer = []

    for target in targets:

        sumKey = 0
       

        for word in target:

            minKey = 101
            flag = False
                
            for key in keymap:    

                if word in key:
                    minKey = min(key.index(word) +1, minKey)
                    flag = True

            if not flag:
                sumKey = -1
                break
            
            sumKey += minKey

 
        answer.append(sumKey)
    
    return answer

keymap = ["AA"]
targets = ["B"]
print(solution(keymap,targets))
