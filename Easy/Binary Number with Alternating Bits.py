class Solution:

    def hasAlternatingBits(self, n: int) -> bool:
        x = bin(n)[2:]
        if "0" in x[::2]:
            return False
        if "1" in x[1::2]:
            return False
        return True