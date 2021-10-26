class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        MOD = 10**9 + 7
        if n < 0:
            print('incorrect input')
        elif n == 0:
            return a
        elif n == 1:
            return b
        else:
            for i in range(2, n+1):
                c = (a + b) % MOD
                a = b
                b = c
            return b

a = Solution()
print(a.fib(8))