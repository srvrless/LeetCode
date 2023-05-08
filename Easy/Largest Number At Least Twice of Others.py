class Solution:

    def dominantIndex(self, nums: List[int]) -> int:
        numsa = sorted(nums)
        if numsa[-1] >= numsa[-2] * 2:
            return nums.index(numsa[-1])
        else:
            return -1