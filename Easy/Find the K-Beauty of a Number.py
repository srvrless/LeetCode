class Solution:

    def divisorSubstrings(self, num: int, k: int) -> int:
        x = str(num)
        c = 0
        for i in range(len(x) - k + 1):
            y = int(x[i:i + k])
            if y == 0:
                continue
            if num % y == 0:
                c += 1
        return c
