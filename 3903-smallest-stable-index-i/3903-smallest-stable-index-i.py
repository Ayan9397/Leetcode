class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Precompute the minimum suffix array
        min_suffix = [0] * n
        min_suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(nums[i], min_suffix[i + 1])
            
        max_prefix = float('-inf')
        
        # Iterate to find the first stable index
        for i in range(n):
            max_prefix = max(max_prefix, nums[i])
            
            # Check the instability score
            if max_prefix - min_suffix[i] <= k:
                return i
                
        return -1
        