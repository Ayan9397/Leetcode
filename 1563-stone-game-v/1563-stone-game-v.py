from functools import cache
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        
        # Precompute prefix sums for O(1) subarray sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= j:
                return 0
                
            ans = 0
            left_sum = 0
            right_sum = prefix[j + 1] - prefix[i]
            
            for k in range(i, j):
                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]
                
                # Bob throws the right row
                if left_sum < right_sum:
                    # Pruning: The max score from dfs(i, k) is at most left_sum. 
                    if ans >= left_sum * 2:
                        continue
                    ans = max(ans, left_sum + dfs(i, k))
                    
                # Bob throws the left row
                elif left_sum > right_sum:
                    # Pruning: As k increases, right_sum only decreases. 
                    # If ans is already >= right_sum * 2, no further k will yield a better answer.
                    if ans >= right_sum * 2:
                        break
                    ans = max(ans, right_sum + dfs(k + 1, j))
                    
                # Alice chooses the row
                else:
                    ans = max(ans, left_sum + max(dfs(i, k), dfs(k + 1, j)))
                    
            return ans

        return dfs(0, n - 1)