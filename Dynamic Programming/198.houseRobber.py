def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return dp[-1]


print(rob([1, 2, 3, 1]))



def rob(nums):
    # [rob1, rob2, n, n + 1, n + 2]
    rob1, rob2 = 0, 0
    for n in nums:
        newRob = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = newRob
    return rob2
