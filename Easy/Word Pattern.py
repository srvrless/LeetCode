class Solution:
    def wordPattern(self,pattern: str, s: str):
        z = list(zip(s.split(), list(pattern)))
        if  len(pattern) == len(s.split()) and len(set(z)) == len(set(s.split())) and len(set(z)) == len(set(pattern)):
            return True
        else:
            return False