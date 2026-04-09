class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        seen = set()

        res = []
        sol = []
        def dfs():

            if len(sol) == len(nums):
                res.append(sol[:])
                return

            
            for n in nums:
                if n in seen:
                    continue
                seen.add(n)
                sol.append(n)
                dfs()
                seen.discard(n)
                sol.pop()
        dfs()
        return res