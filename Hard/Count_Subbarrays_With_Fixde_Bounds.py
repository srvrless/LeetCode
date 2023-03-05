class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        last_min = last_max = -1
        start = -1

        res = 0
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                start = i
            if num == minK:
                last_min = i
            if num == maxK:
                last_max = i
            if last_min > start and last_max > start:
                res += min(last_min, last_max) - start

        return res