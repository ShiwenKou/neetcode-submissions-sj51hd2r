class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mappings = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        sol = []
        

        def dfs(i):
            if i == len(digits):
                res.append(''.join(sol))
                return
            
            for c in mappings[digits[i]]: # 'abc'

                sol.append(c)
                dfs(i+1) # each recursive call have another 3-4 recursivecalls
                sol.pop()
        dfs(0)
        return res if digits else []