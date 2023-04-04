class Solution:
    def sumBase(self, val: int, base: int) -> int:
        res = ''
        while val > 0:
            res = str(val % base) + res
            val //= base # for getting integer division
        if res:
             return sum([int(x) for x in res])
        return '0'