class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        add = (sum(aliceSizes)-sum(bobSizes)) // 2

        sets = set(aliceSizes)

        for num in bobSizes:
            if num + add in sets: 
                return [num+add, num]