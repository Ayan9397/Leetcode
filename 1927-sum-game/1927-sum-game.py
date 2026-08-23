class Solution:
    def sumGame(self, num):
        n = len(num)
        mid = n // 2

        left_sum = sum(int(c) for c in num[:mid] if c != '?')
        right_sum = sum(int(c) for c in num[mid:] if c != '?')

        left_q = num[:mid].count('?')
        right_q = num[mid:].count('?')

        return 2 * (left_sum - right_sum) != 9 * (right_q - left_q)