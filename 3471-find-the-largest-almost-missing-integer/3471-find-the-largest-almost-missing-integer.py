from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Case 1: Subarray size is the entire array length
        if k == n:
            return max(nums)
            
        # Count frequencies of all elements in the array
        counts = Counter(nums)
        
        # Case 2: Subarray size is 1
        if k == 1:
            ans = -1
            for num, freq in counts.items():
                if freq == 1:
                    ans = max(ans, num)
            return ans
            
        # Case 3: 1 < k < n
        # Only the extreme ends of the array can possibly appear in exactly 1 subarray
        ans = -1
        
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
            
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans