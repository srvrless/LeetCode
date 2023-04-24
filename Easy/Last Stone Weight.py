class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            s1 = stones.pop(stones.index(max(stones)))
            s2 = stones.pop(stones.index(max(stones)))
            stones.append(s1 - s2)
        return stones[0]