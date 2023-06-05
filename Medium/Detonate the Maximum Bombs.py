class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        count=1
        res=[]
        for i in range(len(bombs)-1):
            x=bombs[i][0]+bombs[i][1]
            x1=bombs[i+1][0]+bombs[i+1][1]
            if abs(x-x1)<=bombs[i+1][2]:
                count+=1
                res.append(i)
        return count