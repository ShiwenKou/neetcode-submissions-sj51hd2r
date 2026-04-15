class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res, sol = [], []
        def dfs(start):
            if start == len(s):
                res.append(sol[:])
                return
            

            for end in range(start, len(s)):
                sub = s[start : end + 1]
                if sub == sub[::-1]:
                    sol.append(sub)
                    dfs(end + 1)
                    sol.pop()
        dfs(0)
        return res
