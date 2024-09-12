def solution(s, n):

    result=''

    for char in s:
        if char!=" ":
            ordVal = (ord(char) + n)

            if ((ord('A') <= ord(char) <= ord('Z') and ordVal > ord('Z'))
                    or (ord('a') <= ord(char) <= ord('z') and ordVal > ord('z'))):
                ordVal -= 26

            result += chr(ordVal)
        else:
            result += char
      
    return result
 
s="a B Z"
n=4
print(solution(s,n))