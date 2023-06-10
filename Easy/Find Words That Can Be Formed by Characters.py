class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def helper(word, chars):
            for i in word:
                if i not in chars:
                    return 0
                else:
                    if word.count(i) > chars.count(i):
                        return 0
            return len(word)
        
        res = 0
        for word in words:
            res += helper(word, chars)
        return res
