class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for i in range(len(strs[0])):
            if any(strs[j][i] > strs[j + 1][i] for j in range(len(strs) - 1)):
                res += 1
        return res