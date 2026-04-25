class Solution:
    def myPow(self, x: float, n: int) -> float:

        def dfs(n):
            if n == 1:
                return x
            if n == 0:
                return 1
            half = dfs(n // 2)
            if n % 2:
                res = half * half  * x
            else:
                res = half * half

            return res
        if n < 0:
            x = 1 / x
            n = -n
        return dfs(n)