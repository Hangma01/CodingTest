def solution(s):
    dic = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
          7: 'seven', 8: 'eight', 9: "nine"}
   
    for i in range(len(dic)):
        if dic[i] in s:
            s = s.replace(dic[i],str(i))
            
    return int(s)

s="one4seveneight"
print(solution(s))