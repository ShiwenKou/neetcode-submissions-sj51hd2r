class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}
        def dfs(r, c):
            if r == len(word1):
                return len(word2) - c #这里的意思是。word1已经处理完了。但是word2还多，我们insert进入一个尾巴就好？

            if c == len(word2):
                return len(word1) - r #这里的意思是不是 c已经用完了。 word1里面还有一些尾巴。删掉就好
            if (r, c) in memo:
                return memo[(r, c)]

            if word1[r] == word2[c]:
                res = dfs(r + 1, c + 1)
            
            else:
                # 3 ways

                res = min(1 + dfs(r+1, c), # remove current char
                           1 + dfs(r+1, c+1), # replace current char
                           1 + dfs(r, c+1)) # insert a char
            memo[(r, c)] = res
            return res
        
        return dfs(0, 0)