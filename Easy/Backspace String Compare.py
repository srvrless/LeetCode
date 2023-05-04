import collections

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        dq = collections.deque([])
        for i in range(len(s)):
            if s[i] == "#":
                if len(dq) == 0:
                    continue
                else:
                    dq.pop()
            else:
                dq.append(s[i])

        dq1 = collections.deque([])
        for i in range(len(t)):
            if t[i] == "#":
                if len(dq1) == 0:
                    continue
                else:
                    dq1.pop()
            else:
                dq1.append(t[i])
        return dq == dq1