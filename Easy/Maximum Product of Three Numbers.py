import math

nums = [-100, -98, -1, 2, 3, 4]
print(sorted(nums, reverse=True))
print(math.prod(sorted(nums, reverse=True)[:3]))
