class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        from functools import cache
        @cache
        def dfs(start):
            if start == len(s):
                return True

            
            for w in wordDict:
                if start + len(w) <= len(s) and s[start: start + len(w)] == w:

                    if dfs(start + len(w)):
                        return True
            return False
        
        return dfs(0)