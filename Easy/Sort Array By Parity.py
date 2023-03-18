class Solution:

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        x1 = [x for x in nums if x % 2 == 0]
        x2 = [x for x in nums if x % 2 != 0]
        x1.extend(x2)
        return x1