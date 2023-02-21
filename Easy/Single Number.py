from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict = Counter(nums)
        sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
        return sorted_dict[0][0]
