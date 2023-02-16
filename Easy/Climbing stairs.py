class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        k2 = 2
        k3 = 3

        for i in range(n - 3):
            k3, k2 = k3 + k2, k3

        return k3