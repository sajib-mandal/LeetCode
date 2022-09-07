# Time O(n) 
# Space O(1)

import math
def buildArray(nums):
    n = len(nums)
    for i in range(len(nums)):
        nums[i] = n * (nums[nums[i]] % n) + nums[i]
    for i in range(len(nums)):
        nums[i] = math.floor(nums[i] / n)

    return nums


print(buildArray([0, 2, 1, 5, 3, 4]))
print(buildArray([5, 0, 1, 2, 3, 4]))


# same aproch
def buildArray(nums):
    n = len(nums)
    
    for i in range(len(nums)):
        nums[i] = n * (nums[nums[i]] % n) + nums[i]
        
    for i in range(len(nums)):
        nums[i] = nums[i] // n

    return nums


print(buildArray([0, 2, 1, 5, 3, 4]))
print(buildArray([5, 0, 1, 2, 3, 4]))


# same aproch

def buildArray(nums):
    n = len(nums)

    for i in range(len(nums)):
        nums[i] = n * (nums[nums[i]] % n) + nums[i]

    for i in range(len(nums)):
        nums[i] = int(nums[i] / n)

    return nums


print(buildArray([0, 2, 1, 5, 3, 4]))
print(buildArray([5, 0, 1, 2, 3, 4]))



# Time O(n)
# Space O(n)


def buildArray(nums):
    res = []
    for i in range(len(nums)):
        res.append(nums[nums[i]])
    return res


print(buildArray([0, 2, 1, 5, 3, 4]))
print(buildArray([5, 0, 1, 2, 3, 4]))
