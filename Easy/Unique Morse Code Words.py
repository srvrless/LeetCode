class Solution:

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        negr = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        res = ""
        for i in words:
            for x in i:
                res += (negr[(ord(x) - 97)])
            res += "|"
        return (len(set(res[:-1].split("|"))))