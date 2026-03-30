class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        sol = []
        def dfs(j):
            if j == len(s):
                res.append(sol[:])
                return

            for i in range(j, len(s)):
                substring = s[j: i + 1]
                if substring == substring[::-1]:
                    sol.append(substring)
                    dfs(i + 1)
                    sol.pop()
        dfs(0)
        return res