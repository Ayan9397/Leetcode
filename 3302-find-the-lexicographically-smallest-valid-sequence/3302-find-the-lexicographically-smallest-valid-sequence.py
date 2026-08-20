class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        exact = [m] * (n + 1)

        almost = [m] * (n + 1)

        for i in range(n - 1, -1, -1):

          
            exact[i] = exact[i + 1]

            if exact[i + 1] > 0:
                j = exact[i + 1] - 1

                if word1[i] == word2[j]:
                    exact[i] = j

            # -------------------------
            # Compute almost[i]
            # -------------------------
            almost[i] = almost[i + 1]

            if almost[i + 1] > 0:
                j = almost[i + 1] - 1

                if word1[i] == word2[j]:
                    almost[i] = min(almost[i], j)

            if exact[i + 1] > 0:
                j = exact[i + 1] - 1
                almost[i] = min(almost[i], j)


        ans = []
        j = 0
        used_mismatch = False

        for i in range(n):

            if j == m:
                break

            # Option 1: characters already match
            if word1[i] == word2[j]:

                if almost[i + 1] <= j + 1:
                    ans.append(i)
                    j += 1

            # Option 2: use our one mismatch
            elif not used_mismatch:

                if exact[i + 1] <= j + 1:
                    ans.append(i)
                    j += 1
                    used_mismatch = True

        if j != m:
            return []
        return ans