def solution(n, lost, reserve):
    intersection = set(lost) & set(reserve)
    lost = set(lost) - intersection
    reserve = set(reserve) - intersection

    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
 
        elif i+1 in lost:
            lost.remove(i+1)

    return n-len(lost)

n=10
lost=[1, 2, 3, 4, 5, 6]
reserve=[1,2,3]
print(solution(n,lost,reserve))