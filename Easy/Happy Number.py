class Solution:
    def isHappy(self, n):
        def nothappy(n):
            if n == 1:
                return True
            if n < 6:
                return False

            s = sum([(int(x) ** 2) for x in str(n)])
            return nothappy(s)

        return nothappy(n)
