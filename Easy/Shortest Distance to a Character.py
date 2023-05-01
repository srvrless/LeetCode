class Solution:

    def shortestToChar(self, s: str, c: str) -> List[int]:
        shortest_distance = [0] * len(s)
        ind = s.index(c)
        for i in range(len(s)):
            if abs(ind - i) > abs(s.find(c, i) - i):
                ind = s.index(c, i)
            if s[i] != c:
                shortest_distance[i] = abs(ind - i)
        return shortest_distance