class Solution:

    def distributeCandies(self, candyType: List[int]) -> int:
        s1 = len(candyType) // 2
        gosling = len(Counter(candyType))
        if s1 > gosling:
            return gosling
        else:
            return s1