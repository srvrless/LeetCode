class Solution:

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        asn = 0
        nertg = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nertg += 1
            if nertg > asn:
                asn = nertg
            elif nums[i] >= nums[i + 1]:
                nertg = 0
        return asn + 1
