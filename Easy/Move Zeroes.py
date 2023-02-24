class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                count += 1
                nums.pop(i)

        for x in range(1, count + 1):
            nums.append(0)
        return nums
