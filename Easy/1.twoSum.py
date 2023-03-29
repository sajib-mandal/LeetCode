def twoSum(nums, target):
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return []

print(twoSum([2,7,11,15], 9)) # [0, 1]
print(twoSum([3, 2, 4], 6)) # [1, 2]
print(twoSum([3, 3], 6)) # [0, 1]
print(twoSum([3, 2, 3], 6)) # [0, 2]
