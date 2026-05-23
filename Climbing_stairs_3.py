class Solution:
    def climbStairs(self, n: int) -> int:
        def ways(n):
            if n <= 2:
                return n

            a = 1   # f(1)
            b = 2   # f(2)

            for _ in range(3, n + 1):
                c = a + b
                a = b
                b = c

            return b
        return ways(n)