class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum = 0
        for i in range(n):
            sum += mat[i][i]  # sum of principal diagonal
            sum += mat[i][n - i - 1]  # sum of counter diagonal

        if n % 2 == 1:
            sum -= mat[n // 2][n // 2]
        return sum