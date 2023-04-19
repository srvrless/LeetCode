class Solution:

    def numberOfSteps(self, num: int) -> int:
        count = 0
        for i in range(num):
            if num == 0:
                return count
            if num % 2 == 0:
                count += 1
                num /= 2
            if num % 2 != 0:
                count += 1
                num -= 1
        return count