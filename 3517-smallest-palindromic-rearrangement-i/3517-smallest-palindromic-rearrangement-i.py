from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)

        left = ""
        middle = ""

        for ch in sorted(count):
            left += ch * (count[ch] // 2)

            if count[ch] % 2:
                middle = ch

        return left + middle + left[::-1]