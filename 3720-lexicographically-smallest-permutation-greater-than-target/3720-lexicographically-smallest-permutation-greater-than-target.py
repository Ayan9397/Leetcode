from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        # Step 1: Build the longest possible prefix that matches `target`
        i = 0
        while i < n and counts[target[i]] > 0:
            counts[target[i]] -= 1
            i += 1
            
        # If we matched the target perfectly, we need to backtrack by one 
        # position because we are looking for a *strictly* greater string.
        if i == n:
            i -= 1
            counts[target[i]] += 1
            
        # Step 2: Traverse backwards to find the best point to diverge
        for j in range(i, -1, -1):
            
            # Look for the smallest available character strictly greater than target[j]
            best_char = None
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char > target[j] and counts[char] > 0:
                    best_char = char
                    break
                    
            if best_char:
                # We found a valid character to diverge at index j
                counts[best_char] -= 1
                
                # Gather all remaining characters in lexicographical (ascending) order
                remaining = []
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if counts[char] > 0:
                        remaining.append(char * counts[char])
                        
                # Construct and return the result
                return target[:j] + best_char + "".join(remaining)
            
            # If no valid character was found for index j, we step back
            # and restore target[j-1] to our pool of available characters.
            if j > 0:
                counts[target[j - 1]] += 1
                
        # If we exhaust all indices and can't find a valid permutation
        return ""