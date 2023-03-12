from math import sqrt


class Solution:

    def isPerfectSquare(self, num: int) -> bool:
        x = str(sqrt(num))
        if x[-1] == '0':
            return True