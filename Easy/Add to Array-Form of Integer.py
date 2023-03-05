class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        x= int(''.join([str(x) for x in num]))+k
        return [int(s) for s in str(x)]