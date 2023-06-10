class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def fn(n, x):
            if n < x:
                return n * (2 * x - n + 1) // 2
            return x * (1 + x) // 2 + n - x

        # last true binary search
        lo, hi = 0, maxSum
        while lo < hi:
            mid = lo + hi + 1 >> 1
            sm = fn(index, mid - 1) + fn(n - index, mid)
            if sm <= maxSum:
                lo = mid
            else:
                hi = mid - 1
        return lo
