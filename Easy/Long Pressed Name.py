class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        dick = 0
        for i in range(len(typed)):
            if dick < n and name[dick] == typed[i]:
                dick+=1
            elif i == 0 or typed[i] != typed[i-1]:
                return False
        return dick == n