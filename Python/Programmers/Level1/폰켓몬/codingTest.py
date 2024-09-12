def solution(nums):
    count = len(nums) // 2
    typeLen = len(set(nums))
    return typeLen if typeLen < count else count

nums=[3,3,3,2,2,2]
print(solution(nums))