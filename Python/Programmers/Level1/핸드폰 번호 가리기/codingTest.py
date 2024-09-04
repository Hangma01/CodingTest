def solution(phone_number):
    phoneLen = len(phone_number)
    return "*"*(phoneLen-4) + phone_number[phoneLen-4:phoneLen+1]

phone_number="01033334444"
print(solution(phone_number))