class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        


        word_set = set(wordDict)

        memo = {}
        def dfs(start):

            if start == len(s):
                return True
            if start in memo:
                return memo[start]

            for end in range(start, len(s)):
                sub = s[start: end + 1]
                if sub in word_set:
                    if dfs(end + 1):
                        memo[start] = True
                        return True
            memo[start] = False
            return False
        
        return dfs(0)