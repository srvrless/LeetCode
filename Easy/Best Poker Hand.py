class Solution:

    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        s = Counter(suits)
        s1 = Counter(ranks)
        if 5 in s.values():
            return 'Flush'
        if 4 in s1.values():
            return 'Three of a Kind'
        if 3 in s1.values():
            return 'Three of a Kind'
        if 2 in s1.values():
            return 'Pair'
        return "High Card"