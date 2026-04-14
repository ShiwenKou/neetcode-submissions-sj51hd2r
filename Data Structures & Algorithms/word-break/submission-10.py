class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from functools import cache
        word_set = set(wordDict)

        @cache
        def dfs(start):
            if start == len(s):
                return True

            


            for end in range(start, len(s)):
                sub = s[start: end + 1]
                if sub in word_set:
                    if dfs(end + 1):
                        return True
            return False
        
        return dfs(0)