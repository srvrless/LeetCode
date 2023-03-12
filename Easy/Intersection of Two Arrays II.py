class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        a = Counter(nums1)
        b = Counter(nums2)
        l = []
        for i, j in a.items():
            if i in b:
                l += [i] * min(j, b[i])
        return l