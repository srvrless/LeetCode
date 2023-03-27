class Solution:

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dick = {}
        res = []
        arr1 = sorted(list(set(arr)))
        for i in range(len(arr1)):
            dick[arr1[i]] = i + 1
        for i in arr:
            res.append(dick[i])
        return res