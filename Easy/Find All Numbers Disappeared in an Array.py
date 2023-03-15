class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        max_set = set(nums)
        stack = []
        for i in range(1, len(nums) + 1):
            if i not in max_set:
                stack.append(i)
        return stack