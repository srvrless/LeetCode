from itertools import accumulate


class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        x = list(accumulate(sorted(satisfaction, reverse=True)))

        return sum(i for i in x if i > 0)