def solution(data, ext, val_ext, sort_by):
   
    standard = {"code" : 0, "date" : 1,"maximum" : 2, "remain" : 3 }
    result=[]
    for val in data:
        if val[standard[ext]] < val_ext:
            result.append(val)
    
    result.sort(key=lambda x:x[standard[sort_by]])

    return result



data=[[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext="date"
val_ext=20300501
sort_by="remain"
print(solution(data,ext,val_ext,sort_by))