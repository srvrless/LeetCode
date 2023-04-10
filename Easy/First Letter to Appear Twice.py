class Solution:

    def repeatedCharacter(self, s: str) -> str:
        res = []
        try:
            for i in range(len(s)):
                res.append(s[i])
                if s[i + 1] in res:
                    return s[i + 1]
        except:
            return s[i + 1]
