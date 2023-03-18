class Solution:

    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        return [
            x for x in words if all(x.lower() in row2 or x.lower() in row1)
        ]
