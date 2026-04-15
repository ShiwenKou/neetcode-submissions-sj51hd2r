class Solution:
    def myPow(self, x: float, n: int) -> float:

        def dfs(n):
            if n == 1:
                return x
            if n == -1:
                return 1/x
            if n == 0:
                return 1

            res = 1
            if n % 2:
                half = dfs(n // 2)
                res = half * half  * x
            else:
                half = dfs(n // 2)
                res = half * half

            return res
        return dfs(n)