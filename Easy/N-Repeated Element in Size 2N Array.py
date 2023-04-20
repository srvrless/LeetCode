class Solution:

    def repeatedNTimes(self, nums: List[int]) -> int:
        stats = Counter(nums)
        return max(stats, key=stats.get)
