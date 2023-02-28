import operator
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = (Counter(nums))
        sorted_x = sorted(s.items(), key=operator.itemgetter(1))
        return sorted_x[-1][0]
