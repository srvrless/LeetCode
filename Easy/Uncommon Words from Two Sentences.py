class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        allWordsList = s1.split(' ') + s2.split(' ')
        words = Counter(allWordsList)
        
        output = []
        
        for word in words:
            if words[word] == 1:
                output.append(word)
                
        return output
		