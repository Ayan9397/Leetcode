import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        
        mid_char = ""
        counts = [0] * 26
        
        # Count frequencies for the first half of the palindrome
        for char, count in freq.items():
            if count % 2 != 0:
                mid_char = char
            if count // 2 > 0:
                counts[ord(char) - ord('a')] = count // 2
                
        N = sum(counts)
        
        # Calculate initial total permutations for the first half
        total_perms = math.factorial(N)
        for count in counts:
            if count > 1:
                total_perms //= math.factorial(count)
                
        # Return empty string if k exceeds total valid permutations
        if k > total_perms:
            return ""
            
        first_half = []
        
        # Build the first half left to right using combinatorics 
        while N > 0:
            for i in range(26):
                if counts[i] > 0:
                    # Calculate permutations if we place character 'i' at the current position
                    perms_with_this_char = total_perms * counts[i] // N
                    
                    if k <= perms_with_this_char:
                        # Lock in this character, it's the correct choice for this position
                        first_half.append(chr(i + ord('a')))
                        counts[i] -= 1
                        total_perms = perms_with_this_char
                        N -= 1
                        break
                    else:
                        # Skip this character and reduce k by the number of skipped permutations
                        k -= perms_with_this_char
                        
        ans_half = "".join(first_half)
        
        # Construct the final palindrome: Left Half + Middle (if any) + Right Half (reversed left)
        return ans_half + mid_char + ans_half[::-1]