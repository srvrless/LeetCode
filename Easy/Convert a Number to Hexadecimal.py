class Solution:

    def toHex(self, num: int) -> str:
        return format(num & 0xffffffff, 'x')