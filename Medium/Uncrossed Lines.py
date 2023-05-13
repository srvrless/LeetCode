class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i1 in range(n1 - 1, -1, -1):
            for i2 in range(n2 - 1, -1, -1):
                if nums1[i1] == nums2[i2]:
                    dp[i1][i2] = 1 + dp[i1+1][i2+1]
                else:
                    dp[i1][i2] = max(dp[i1+1][i2], dp[i1][i2+1])

        return dp[0][0] 







# class Solution:
#     def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
#         @lru_cache(None)
#         def max_lines(i, j):
#             if i == len(nums1) or j == len(nums2):
#                 return 0
#             else:
#                 res = max(max_lines(i+1, j), max_lines(i, j+1))
#                 if nums1[i] == nums2[j]:
#                     res = max(res, 1+ max_lines(i+1, j+1))
#                 return res
                    
#         return max_lines(0,0)