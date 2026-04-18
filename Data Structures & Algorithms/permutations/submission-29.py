class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        sol = []
        res = []
        seen = set()
        def dfs():

            if len(sol) == len(nums):
                res.append(sol[:])
                return

            
            for n in nums:
                if n not in seen:
                    seen.add(n)
                    sol.append(n)
                    dfs()
                    seen.remove(n)
                    sol.pop()
        
        dfs()
        return res
