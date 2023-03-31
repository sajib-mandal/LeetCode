def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    return max(helper(nums[1:]), helper(nums[:-1]))

def helper(nums):
    # [rob1, rob2, n, n + 1, n + 2]
    rob1, rob2 = 0, 0
    for n in nums:
        newRob = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = newRob
    return rob2

print(rob([2, 3, 2])) # 3
print(rob([1, 2, 3, 1])) # 4
print(rob([1, 2, 3])) # 3
