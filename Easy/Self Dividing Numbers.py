class Solution:

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def self_divide(x: int):

            y = str(x)
            if "0" in y:
                return False

            for t in y:
                if x % int(t) != 0:
                    return False
            return True

        reult = []

        for i in range(left, right + 1):
            if self_divide(i):
                reult.append(i)

        return reult