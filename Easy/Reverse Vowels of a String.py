class Solution:
    def reverseVowels(self, string: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        chars = list(string)
        left, right = 0, len(chars) - 1
        while left < right:
            if chars[left].lower() not in vowels:
                left += 1
            elif chars[right].lower() not in vowels:
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return ''.join(chars)