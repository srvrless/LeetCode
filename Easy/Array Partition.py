class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        re1 = []
        nums = sorted(nums)
        try:
            for i in range(0, len(nums), 2):
                x = [nums[i], nums[i + 1]]
                re1.append(min(x))
            return sum(re1)
        except ValueError:
            return sum(re1)
