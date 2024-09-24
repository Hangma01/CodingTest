def solution(numbers, hand):
    keyPad = {1 : [0,0], 2 : [0,1], 3 : [0,2],
              4 : [1,0], 5 : [1,1], 6 : [1,2],
              7 : [2,0], 8 : [2,1], 9 : [2,2],
              0 : [3,1]
              }
    
    leftFinger = [3,0]
    rightFinger = [3,2]
    onlyLeft = [1,4,7]
    onlyRight = [3,6,9]
    result = []

    for number in numbers:

        if number in onlyLeft:
            result.append('L')
            leftFinger = keyPad[number]
        elif number in onlyRight:
            result.append('R')
            rightFinger = keyPad[number]
        else:
            left = (abs(leftFinger[0] - keyPad[number][0]) + abs(leftFinger[1] - keyPad[number][1]))
            right = (abs(rightFinger[0] - keyPad[number][0]) + abs(rightFinger[1] - keyPad[number][1]))

            if left > right:
                result.append('R')
                rightFinger = keyPad[number]
            elif left < right:
                result.append('L')
                leftFinger = keyPad[number]
            else:
                if hand == "right":
                    result.append('R')
                    rightFinger = keyPad[number]
                elif hand == "left":
                    result.append('L')
                    leftFinger = keyPad[number]

    return ''.join(result)

numbers=[0,0]
hand="right"
print(solution(numbers,hand))