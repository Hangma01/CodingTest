def solution(t, p):
    
    ti = int(t)
    pi = int(p)
    plen = len(p)
    tlen = len(t)

    count = 0

    while True:

        po = pow(10,(tlen - plen))
        to = ti // po
        if to <= pi:
            count += 1
        
        ti = ti % pow(10,tlen-1)

        if tlen == plen:
            return count
        
        tlen -= 1


t = "10203"
p = "15"
print(solution(t,p))
