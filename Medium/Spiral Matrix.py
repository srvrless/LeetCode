class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = cols - 1
        top = 0
        bottom = rows - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for j in range(top, bottom + 1):
                result.append(matrix[j][right])
            right -= 1

            if top <= bottom:
                for k in range(right, left - 1, -1):
                    result.append(matrix[bottom][k])
                bottom -= 1

            if left <= right:
                for x in range(bottom, top - 1, -1):
                    result.append(matrix[x][left])
                left += 1

        return result