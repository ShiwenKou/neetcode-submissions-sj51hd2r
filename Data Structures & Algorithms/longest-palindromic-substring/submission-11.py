class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        memo = {}
        def dfs(i, j):
            if i >= j:
                return True # means we nv encounter s[i] != s[j] as we shrink the range
            
            if s[i] != s[j]:
                return False
            if (i, j) in memo:
                return memo[(i, j)]
            ans = dfs(i + 1, j - 1) 

            memo[(i, j)] = ans
            return ans




        best_i, best_j = 0, 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dfs(i, j) and j - i > best_j - best_i:
                    best_i, best_j = i, j

        return s[best_i: best_j + 1]