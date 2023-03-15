class Solution:

    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]

        for divider in range(0, len(nums) - 1):
            ans = min(
                ans,
                max(nums[divider] + k, nums[-1] - k) -
                min(nums[divider + 1] - k, nums[0] + k))

        return ans