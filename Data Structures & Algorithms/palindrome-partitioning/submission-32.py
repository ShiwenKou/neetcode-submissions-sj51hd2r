class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        sol = []
        res = []

        def dfs(start):

            if start == len(s):
                res.append(sol[:])
                return

            
            for end in range(start, len(s)):
                substring = s[start: end + 1]

                if substring == substring[::-1]:
                    sol.append(substring)
                    dfs(end + 1)
                    sol.pop()

        dfs(0)
        return res