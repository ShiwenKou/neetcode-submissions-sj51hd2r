class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        from functools import cache # memoization
        wordSet = set(wordDict)
        @cache
        def dfs(start):
            if start == len(s):
                return True

            
            for end in range(start, len(s)):
                sub = s[start : end + 1] # len(s) is exclusive
                if sub in wordSet:
                    if dfs(end + 1):
                        return True
            return False

        return dfs(0)