class Solution:
    def longestCommonPrefix(self, strs):
        ans = ""

        for chars in zip(*strs):
            if len(set(chars)) == 1:
                ans += chars[0]
            else:
                break

        return ans