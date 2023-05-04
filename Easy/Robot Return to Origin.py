from collections import Counter

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counted_moves = Counter(moves)
        return (counted_moves['U'] == counted_moves['D']) and (counted_moves['L'] == counted_moves['R'])