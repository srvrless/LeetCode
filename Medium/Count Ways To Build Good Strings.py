class Solution:

    def countGoodStrings(self, low: int, high: int, a: int, b: int) -> int:
        ct = 0
        lst = [-1] * (high + 1)

        def sol(a, b, lst, i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            if lst[i] != -1:
                return lst[i]
            lst[i] = sol(a, b, lst, i - a) + sol(a, b, lst, i - b)
            return lst[i]

        for i in range(low, high + 1):
            ct += sol(a, b, lst, i)
        return ct % (10**9 + 7)
