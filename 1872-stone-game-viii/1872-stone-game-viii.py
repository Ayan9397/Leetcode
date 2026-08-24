class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        
        # P[n-1] is just the sum of all stones
        current_prefix_sum = sum(stones)
        
        # Base case: dp[n-1] = P[n-1]
        dp = current_prefix_sum
        
        # Iterate backwards from n-2 down to 1
        # We stop at 1 because x > 1 (the player must pick at least 2 stones initially)
        for i in range(n - 1, 1, -1):
            # Update current_prefix_sum to P[i-1] by subtracting stones[i]
            current_prefix_sum -= stones[i]
            
            # dp[i] = max(take, skip)
            # take = current_prefix_sum - dp
            # skip = dp
            dp = max(current_prefix_sum - dp, dp)
            
        return dp