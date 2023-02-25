class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        x = sorted(t)
        try:
            for i in range(0, len(s) + 1):
                if s[i] != x[i]:
                    return x[i]
        except:
            return x[-1]
