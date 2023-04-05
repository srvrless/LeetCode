class Solution:

    def bitwiseComplement(self, n: int) -> int:
        bi = bin(n)[2:]
        x = {"1": "0", "0": "1"}
        tbl = bi.maketrans(x)
        return int(bi.translate(tbl), 2)
