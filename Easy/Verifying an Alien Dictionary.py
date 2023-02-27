class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        charOrder = {}
        for i in range(len(order)):
            charOrder[order[i]] = i
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            len_ = min(len(word1), len(word2))
            for j in range(len_):
                if word1[j] != word2[j]:
                    if charOrder[word1[j]] > charOrder[word2[j]]:
                        return False
                    else:
                        break
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return False
        return True
