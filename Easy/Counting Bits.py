class Solution:
    def countBits(self, n: int) -> List[int]:
        return [int((bin(i)[2:]).count('1')) for i in range(0,n+1)]