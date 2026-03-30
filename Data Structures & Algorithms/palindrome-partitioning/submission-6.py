class Solution:
    def partition(self, s: str) -> List[List[str]]:

        sol = []
        res = []

        def dfs(i):
            if i == len(s):
                res.append(sol[:])
                return
            
            for j in range(i, len(s)):
                substring = s[i: j + 1] # 'aab' 1-> 'a'. 2->'aa' 3->'aab'
                if substring == substring[::-1]:
                    sol.append(substring)
                    dfs(j + 1) # deal with 'ab'
                    sol.pop()
        dfs(0)
        return res