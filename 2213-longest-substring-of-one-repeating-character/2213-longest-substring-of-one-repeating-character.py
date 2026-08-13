from typing import List


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)

        # Each node stores:
        # (left_char, right_char, prefix, suffix, best, length)
        tree = [None] * (4 * n)

        def merge(a, b):
            left_char, right_char, prefix, suffix, best, length = a
            left_char2, right_char2, prefix2, suffix2, best2, length2 = b

            # -------------------------
            # Prefix
            # -------------------------
            new_prefix = prefix

            # Entire left segment is one character
            # and it matches the first character of right
            if prefix == length and right_char == left_char2:
                new_prefix = length + prefix2

            # -------------------------
            # Suffix
            # -------------------------
            # IMPORTANT:
            # Normally suffix comes from the RIGHT segment.
            new_suffix = suffix2

            # Entire right segment is one character
            # and it matches the last character of left
            if suffix2 == length2 and right_char == left_char2:
                new_suffix = suffix + length2

            # -------------------------
            # Best
            # -------------------------
            new_best = max(best, best2)

            # If boundary characters are equal,
            # join left suffix + right prefix.
            if right_char == left_char2:
                new_best = max(
                    new_best,
                    suffix + prefix2
                )

            return (
                left_char,
                right_char2,
                new_prefix,
                new_suffix,
                new_best,
                length + length2
            )

        def build(node, left, right):

            if left == right:
                tree[node] = (
                    s[left],  # left character
                    s[left],  # right character
                    1,        # prefix
                    1,        # suffix
                    1,        # best
                    1         # length
                )
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, index, char):

            if left == right:
                tree[node] = (
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                )
                return

            mid = (left + right) // 2

            if index <= mid:
                update(
                    node * 2,
                    left,
                    mid,
                    index,
                    char
                )
            else:
                update(
                    node * 2 + 1,
                    mid + 1,
                    right,
                    index,
                    char
                )

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        # Build initial segment tree
        build(1, 0, n - 1)

        answer = []

        # Process every query
        for char, index in zip(
            queryCharacters,
            queryIndices
        ):
            update(
                1,
                0,
                n - 1,
                index,
                char
            )

            # tree[1][4] = best
            answer.append(tree[1][4])

        return answer