def solution(id_list, report, k):

    report = list(set(report))
    nameDict = {i : 0 for i in id_list}
    messageDict = {i : 0 for i in id_list}
    reportList = [i.split(' ') for i in report]
    

    for report in reportList:
        nameDict[report[1]] += 1

    for name in nameDict:
        if nameDict[name] >= k:
  
            for report in reportList:
                if report[1] == name:
                    messageDict[report[0]] += 1

    return list(messageDict.values())



id_list=["con", "ryan"]
report=["ryan con", "ryan con", "ryan con", "ryan con"]
k=3

print(solution(id_list,report,k))