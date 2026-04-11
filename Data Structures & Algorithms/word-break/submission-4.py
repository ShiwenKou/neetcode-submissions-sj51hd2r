class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dic = set(wordDict)
        
        memo = {}
        def dfs(start):

            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]
            for end in range(start, len(s)):
                substring = s[start: end + 1]
                if substring in dic:
                    if dfs(end + 1):
                        memo[start] = True
                        return True
            memo[start] = False
            return False
        
        if dfs(0):
            return True
        else:
            return False