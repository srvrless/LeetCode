from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts = [(sum(row), i) for i, row in enumerate(mat)]
        counts.sort()

        return [i for _, i in counts[:k]]