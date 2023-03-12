from collections import Counter


class Solution:

    def firstUniqChar(self, s: str) -> int:
        for i, y in Counter(s).items():
            if y == 1:
                return s.index(i)
        return -1