class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prev = []
        for i in range(len(nums)):
            prev.append(nums[i])
            if sum(nums[i:])==sum(prev):
                return i
        return -1