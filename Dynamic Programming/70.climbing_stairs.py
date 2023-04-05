# bottom-up

def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
  
  
  # top-down
  class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n, memo):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in memo:
                return memo[n]

            memo[n] = dfs(n - 1, memo) + dfs(n - 2, memo)
            return memo[n]
        
        return dfs(n, memo)
