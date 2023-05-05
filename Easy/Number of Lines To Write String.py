class Solution:

    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        width = 0
        for c in s:
            w = widths[ord(c) - ord('a')]
            if width + w > 100:
                lines += 1
                width = w
            else:
                width += w
        return [lines, width]
