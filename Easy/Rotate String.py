import collections


class Solution:

    def rotateString(self, s: str, goal: str) -> bool:
        s = [x for x in s]
        dq = collections.deque(s)
        for i in range(len(s)):
            dq.append(s[i])
            dq.popleft()
            if ''.join(dq) == goal:
                return True
        return False