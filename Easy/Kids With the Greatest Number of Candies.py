class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        masx = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= masx:
                result.append(True)
            else:
                result.append(False)
        return result
