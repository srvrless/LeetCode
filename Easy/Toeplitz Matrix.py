class Solution:
    def isToeplitzMatrix(self, A: List[List[int]]) -> bool:
        for i in range(len(A)-1):
            for y in range(len(A[0])-1):
                if A[i][y] != A[i+1][y+1]:
                    return False
        return True