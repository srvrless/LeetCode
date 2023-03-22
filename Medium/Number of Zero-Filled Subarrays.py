class Solution:

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt = x = 0
        for num in nums:
            if num == 0:
                x += 1
                cnt += x
            else:
                x = 0
        return cnt