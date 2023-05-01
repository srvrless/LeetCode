import numpy as np
from typing import List


class Solution:

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr1 = np.array(matrix)
        arr1_transpose = arr1.transpose()
        return arr1_transpose