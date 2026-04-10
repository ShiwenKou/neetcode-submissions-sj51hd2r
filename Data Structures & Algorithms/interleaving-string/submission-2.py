class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        def dfs(r, c):
        
            if r + c == len(s3):
                return True
            if (r, c) in memo:
                return memo[(r, c)]
            res = False
 
            if r < len(s1) and s1[r] == s3[r + c]:
                res = res or dfs(r + 1, c)
            
            if c < len(s2) and s2[c] == s3[r + c]:
                res =  res or dfs(r, c + 1)

            memo[(r, c)] = res
            return res

        return dfs(0, 0)
