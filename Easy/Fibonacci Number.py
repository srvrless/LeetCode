class Solution:

    def fib(self, n: int) -> int:

        def fibos(n):
            if n == 0:
                return 0
            if n in (1, 2):
                return 1
            return fibos(n - 1) + fibos(n - 2)

        return fibos(n)
