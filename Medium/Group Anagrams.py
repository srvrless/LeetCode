class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i in strs:
            scum= ''.join(sorted(i))
            if scum in res:
                res[scum].append(i)
            else:
                res[scum]=[i]
        return list(res.values())