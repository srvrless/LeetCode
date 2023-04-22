class Solution:

    def checkRecord(self, s: str) -> bool:
        count = 0
        if s.count('A') >= 2:
            return False
        for i in range(len(s) - 2):
            if s[i] == 'L' and s[i + 1] == 'L' and s[i + 2] == 'L':
                count += 1
        return False if count >= 1 else True