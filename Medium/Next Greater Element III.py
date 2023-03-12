import itertools


class Solution:

    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        permutations = itertools.permutations(digits)
        sorted_permutations = sorted(
            int(''.join(perm)) for perm in permutations)
        for perm in sorted_permutations:
            if perm > 2147483647:
                return -1
            if perm > n:
                return perm
        return -1