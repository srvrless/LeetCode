class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        lens = len(str1) // len(str2)
        return str1.replace(str2, '')
