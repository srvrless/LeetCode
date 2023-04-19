class Solution:
    def toGoatLatin(self, s: str) -> str:
        alphabe = ['a', 'e', 'i', 'o', 'u']
        result = []
        count = 1
        for x in s.split():
            count += 1
            if x[0].lower() in alphabe:
                result.append(x + 'm' + ('a' * count))
            if x[0].lower() not in alphabe:
                result.append(x[1:] + x[0] + 'm' + ('a' * count))
        return ' '.join(result)