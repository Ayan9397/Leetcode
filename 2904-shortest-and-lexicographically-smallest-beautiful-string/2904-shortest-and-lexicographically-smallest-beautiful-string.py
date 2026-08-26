class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Step 1: Record indices of all '1's
        ones = [i for i, char in enumerate(s) if char == '1']
        
        # Step 2: If we don't have enough '1's
        if len(ones) < k:
            return ""
        
        min_len = float('inf')
        best_str = ""
        
        # Step 3 & 4: Check every valid window of k ones
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            current_len = end - start + 1
            
            sub = s[start:end + 1]
            
            if current_len < min_len:
                min_len = current_len
                best_str = sub
            elif current_len == min_len:
                if sub < best_str:
                    best_str = sub
                    
        return best_str