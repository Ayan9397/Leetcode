from collections import Counter

FACTOR_COUNTS = {
    0: Counter(),
    1: Counter(),
    2: Counter([2]),
    3: Counter([3]),
    4: Counter([2, 2]),
    5: Counter([5]),
    6: Counter([2, 3]),
    7: Counter([7]),
    8: Counter([2, 2, 2]),
    9: Counter([3, 3]),
}


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        primeCount, ok = self._getPrimeCount(t)
        if not ok:
            return "-1"

        factorCount = self._getFactorCount(primeCount)

        if sum(factorCount.values()) > len(num):
            return "".join(str(d) * factorCount[d] for d in range(2, 10))

        primePrefix = sum(
            (FACTOR_COUNTS[int(c)] for c in num),
            start=Counter(),
        )

        firstZero = next((i for i, c in enumerate(num) if c == "0"), len(num))

        if firstZero == len(num) and primeCount <= primePrefix:
            return num

        n = len(num)

        for i in range(n - 1, -1, -1):
            d = int(num[i])

            primePrefix -= FACTOR_COUNTS[d]

            remain = n - i - 1

            if i > firstZero:
                continue

            for nd in range(d + 1, 10):
                need = self._getFactorCount(
                    primeCount - primePrefix - FACTOR_COUNTS[nd]
                )

                if sum(need.values()) <= remain:
                    ones = remain - sum(need.values())

                    return (
                        num[:i]
                        + str(nd)
                        + "1" * ones
                        + "".join(str(x) * need[x] for x in range(2, 10))
                    )

        need = self._getFactorCount(primeCount)

        return (
            "1" * (n + 1 - sum(need.values()))
            + "".join(str(x) * need[x] for x in range(2, 10))
        )

    def _getPrimeCount(self, t):
        cnt = Counter()

        for p in (2, 3, 5, 7):
            while t % p == 0:
                cnt[p] += 1
                t //= p

        return cnt, t == 1

    def _getFactorCount(self, cnt):
        cnt = Counter(cnt)

        c8 = cnt[2] // 3
        rem2 = cnt[2] % 3

        c9 = cnt[3] // 2
        c3 = cnt[3] % 2

        c4 = rem2 // 2
        c2 = rem2 % 2

        c6 = 0

        if c2 and c3:
            c2 = 0
            c3 = 0
            c6 = 1

        if c3 and c4:
            c2 = 1
            c3 = 0
            c4 = 0
            c6 = 1

        return {
            2: c2,
            3: c3,
            4: c4,
            5: cnt[5],
            6: c6,
            7: cnt[7],
            8: c8,
            9: c9,
        }