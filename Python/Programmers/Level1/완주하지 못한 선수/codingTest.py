def solution(participant, completion):
    
    dictionary = {}

    for person in participant:
        if person not in completion:
            return person
        elif person in dictionary:
            dictionary[person] += 1
        else:
            dictionary[person] = 1

    for person in completion:
        dictionary[person] -= 1
    
    for person in dictionary:
        if dictionary[person] == 1:
            return person


participant=["mislav", "stanko", "mislav", "ana", "ana"]
completion=["stanko", "ana", "mislav", "mislav"]
print(solution(participant,completion))