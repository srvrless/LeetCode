nums = [1, 1, 1]
k = 2
import math


def numSubarrayProductLessThanK():
    negr = 0
    for i in range(0, len(nums)):
        for h in range(1, len(nums)):
            x = (nums[i:i + h])
            if math.prod(x) < k:
                negr += 1

    return negr


print(numSubarrayProductLessThanK())
