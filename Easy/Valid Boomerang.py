class Solution:

    def isBoomerang(self, p: List[List[int]]) -> bool:
        [x1, y1], [x2, y2], [x3, y3] = p
        p.sort()
        if (y2 - y1) * (x3 - x2) != (x2 - x1) * (y3 - y2):
            return True
        return False