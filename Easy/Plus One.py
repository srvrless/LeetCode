class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        for i in range(1, size + 1):
            digits[-i] += 1
            digits[-i] %= 10
            if digits[-i] != 0:
                return digits
            elif (i+1) > size:
                digits.insert(0, 1)
                return digits
        return digits