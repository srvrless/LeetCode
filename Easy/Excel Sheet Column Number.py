class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for i in columnTitle:
            total = total * 26 + ord(i) - ord("A") + 1
        return (total)
