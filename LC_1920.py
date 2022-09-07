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
