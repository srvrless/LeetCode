class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([len(str(x)) for x in nums if len(str(x)) % 2 == 0])
