def solution(new_id):
    check=['-', '_', '.']
    result = ''
    new_id = new_id.lower()
    for char in new_id:
        if char.isupper():
            result+=char.lower()
        elif len(result) > 0 and char == '.' and result[-1] == '.':
            continue
        elif char.islower() or char.isdigit() or char in check:
            result+=char
    
    while len(result) > 0 and result[0] == '.':
        result = result[1:]
    while len(result) > 0 and result[-1] == '.':
        result = result[:-1]
        

    if not result:
        result = 'a'

    if len(result) >= 16:
        result = result[:15]
        while len(result) > 0 and result[-1] == '.':
            result = result[:-1]
    elif len(result) <= 2:
        while len(result) < 3:
            result += result[-1]
    
    return result
    
    

new_id=	"...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))