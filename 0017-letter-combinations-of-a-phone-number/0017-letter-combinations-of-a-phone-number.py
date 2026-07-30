from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Handle the edge case of an empty string
        if not digits:
            return []
            
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        res = []
        
        def backtrack(index: int, path: list):
            # If the current combination is the same length as digits, we have a complete word
            if index == len(digits):
                res.append("".join(path))
                return
            
            # Get the letters that the current digit maps to
            possible_letters = phone_map[digits[index]]
            
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving to the next one in the loop
                path.pop()
                
        # Start backtracking from index 0 with an empty path
        backtrack(0, [])
        
        return res