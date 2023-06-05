class Solution:
    def removePalindromeSub(self, s: str) -> int:
        count=0
        for i in range(0, len(s)):
            if s == s[::-1]:
                count += 1
                break
            z=Counter(s)
            s=s.replace(min(z, key=z.get),'')
            count+=1
        return count