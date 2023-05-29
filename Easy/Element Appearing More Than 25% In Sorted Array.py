class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        cont = Counter(arr)
        return max(cont, key=cont.get)