class Solution:

    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0

        def is_prime(n):
            if n == 1:
                return False
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            return True

        for i in range(left, right + 1):
            x = bin(i).count('1')
            if is_prime(x):
                count += 1
        return count