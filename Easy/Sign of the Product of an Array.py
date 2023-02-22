import functools
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sum_of_numbers= (functools.reduce(lambda a, b : a * b, nums))
        if sum_of_numbers>0:
            return 1
        if sum_of_numbers<0:
            return -1
        return 0