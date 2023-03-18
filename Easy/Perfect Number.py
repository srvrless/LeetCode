class Solution:

    def convertToBase7(self, n: int) -> str:
        x = abs(n)
        b = 7
        if x == 0:
            return '0'
        digits = []
        while x:
            digits.append(str(x % b))
            x //= b
        if n < 0:
            digits.append('-')
        return ''.join(digits[::-1])