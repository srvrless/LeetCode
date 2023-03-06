class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res=[]
        for i in range(1,max(arr)+k*2):
            if i not in arr:
                res.append(i)
        return res[k-1]