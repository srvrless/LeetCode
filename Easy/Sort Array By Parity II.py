import itertools


class Solution:

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        s2 = [n for n in nums if n % 2 == 0]
        s1 = [n for n in nums if n % 2 == 1]
        x = list(zip(s2, s1))
        result = list(itertools.chain.from_iterable(x))
        return result
