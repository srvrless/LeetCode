from typing import List, Deque
from collections import deque

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        nums = deque(nums)
        count = 0
        
        while count < k:
            if nums[0] < 0:
                nums[0] = -nums[0]
                nums = deque(sorted(nums))
            else:
                if (k - count) % 2 == 0:
                    break
                else:
                    nums[0] = -nums[0]
            count += 1
            
        return sum(nums)