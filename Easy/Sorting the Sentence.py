class Solution:

    def sortSentence(self, string: str) -> str:
        result = []
        for i in range(len(string.split()) + 1):
            for x in string.split():
                if str(i) in x:
                    result.append(x[:-1])
        return ' '.join(result)