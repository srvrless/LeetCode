class Solution:
    # gigachad/sigma solution
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo = 0
        hi = len(letters) - 1

        while lo <= hi:
            if letters[lo] > target:
                return letters[lo]
            mid = (lo + hi) // 2
            if letters[mid] > target:
                lo += 1
                hi = mid
            else:
                lo = mid + 1

        if letters[-1] > target:
            return letters[-1]
        else:
            return letters[0]


class Solution:
    # pussy solution
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if ord(i) > ord(target):
                return i
        return letters[0]