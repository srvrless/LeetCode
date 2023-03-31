class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        dick = {}
        slaves = 0
        
        for i,e in enumerate(nums):
            dick[e] = i+1
        
        for e in nums :
            if dick.get(e-diff) and dick.get(e+diff):
                slaves += 1
        return slaves
                