class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        d = collections.Counter([c % 2 for c in chips])
        return min(d[0], d[1])