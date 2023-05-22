from typing import List
from collections import Counter
from operator import itemgetter


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        s = sorted(x.items(), key=itemgetter(1))
        return [x[0] for x in s[-k:]]