class Solution:

    def binaryGap(self, n: int) -> int:
        mxas = 0
        bi = bin(n)[2::]
        x = [i for i, y in enumerate(bi) if y == '1']
        try:
            for a in range(len(x)):
                s = x[a] - x[a + 1]
                if abs(s) > mxas:
                    mxas = abs(s)
            return mxas
        except:
            return mxas