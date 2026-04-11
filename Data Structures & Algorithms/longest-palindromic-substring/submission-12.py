class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        memo = {}
        def dfs(i, j):
            if i >= j:
                return True
            
            if s[i] != s[j]:
                return False
            
            if (i, j) in memo:
                return memo[(i, j)]
            

            res = False

            res = res or dfs(i + 1, j - 1)
            memo[(i, j)] = res
            return res



        length = 0
        for i in range(len(s)):
            for j in range(i, len(s)):

                if dfs(i, j) and j - i + 1 > length:
                    res = s[i: j + 1]
                    length = j - i + 1
        return res
